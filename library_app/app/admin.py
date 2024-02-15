from django.contrib import admin
from .models import CustomUser, BookModel, BorrowBookModel

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BookModel)
admin.site.register(BorrowBookModel)