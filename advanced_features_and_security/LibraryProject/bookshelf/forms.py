from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

from django import forms

class ExampleForm(forms.Form):
    # Add your form fields here
    # For example:
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    # ... other fields ...