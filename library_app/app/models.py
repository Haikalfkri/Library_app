from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_by = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="book_images/")
    

