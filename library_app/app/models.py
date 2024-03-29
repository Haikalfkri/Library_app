from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

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
    book = models.ForeignKey(BookModel, blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    adress = models.TextField()
    date_borrow = models.DateTimeField()
    date_return = models.DateTimeField(null=True, blank=True)
    user_image = models.ImageField(upload_to="borrow_user_images/")
    
    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
    @property
    def userImageUrl(self):
        try:
            url = self.user_image.url
        except:
            url = ''
        return url
    
    def save(self, *args, **kwargs):
        
        if self.date_return is None:
            # Decrease the quantity of the borrowed book
            if self.quantity <= self.book.quantity:
                self.book.quantity -= self.quantity
                self.book.save()
            else:
                raise ValueError("Book not available")
        elif self.date_return <= timezone.now():
            self.book.quantity += self.quantity
            self.book.save()
        
        super().save(*args, **kwargs)   
        