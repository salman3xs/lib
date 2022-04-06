from django import forms
from management.models import Book

class BookForm(forms.ModelForm):
    
    class Meta():
        model = Book
        fields = ('author','title','about')