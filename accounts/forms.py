from django import forms
from django.contrib.auth.models import User
from .models import BookList


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class BookProduct(forms.ModelForm):
    class Meta:
        model = BookList
        fields = ['book_title', 'book_author', 'book_edition', 'book_price', 'user_phn', 'book_image']













