from django import forms
from django.forms import widgets, fields
from .models import Book

class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label='Author UUID', required=False)

class PostAuthor(forms.Form):
    name = forms.CharField(label="Name", max_length=150, required=False)
    age = forms.IntegerField(label="Age", max_value=90, required=False)
    email = forms.EmailField(label="Email", required=False )

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {'description':widgets.TextInput}
