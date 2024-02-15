from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default="user")
    

class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_by = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="book_images/")
    
    def __str__(self):
        return self.title
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ""
            
        return url
    

class BorrowBookModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ManyToManyField(BookModel)
    quantity = models.PositiveIntegerField(default=1)
    adress = models.TextField()
    date_borrow = models.DateTimeField()
    date_return = models.DateTimeField()
    user_image = models.ImageField(upload_to="user_images/")
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Decrease the quantity of the borrowed book
        if self.quantity <= self.book.quantity:
            self.book.quantity -= self.quantity
            self.book.save()
        else:
            raise ValueError("Borrow quantity exceeds available quantity")
        
        super().save(*args, **kwargs)