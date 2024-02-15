from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import CustomUser, BookModel, BorrowBookModel


class AdminRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))
    role = forms.ChoiceField(choices=CustomUser.USER_ROLE_CHOICES, widget=forms.Select(attrs={
        'class': 'form-select',
        'placeholder': 'Select a Role'
    }))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','role', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            })
        }
        
    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop('exclude', [])
        super(AdminRegisterForm, self).__init__(*args, **kwargs)
        
        # Exclude specified fields from validation
        for field_name in exclude_fields:
            self.fields.pop(field_name, None)
    
    
class AddBookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ('title', 'author', 'published_by', 'quantity', 'image')
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author',
            }),
            'published_by': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Published By',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'quantity',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
        
        

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BorrowBookModel
        fields = ('user', 'book', 'quantity', 'adress', 'date_borrow', 'date_return', 'user_image')
        
        
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'value': '1',
                'disabled': 'disabled'
            }),
            'adress': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '4'
            }),
            'date_borrow': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
            'date_return': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
            'user_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
        
    
        # Specify the input formats
        input_formats = {
            'date_borrow': ['%Y-%m-%dT%H:%M'],
            'date_return': ['%Y-%m-%dT%H:%M'],
        }