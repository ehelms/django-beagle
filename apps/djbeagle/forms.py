from django import forms
from django.forms import ModelForm

from djbeagle.models import Search

class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = ('name', )
