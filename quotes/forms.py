from django import forms
from django.db.models import fields

from .models import *

class StockForm(forms.ModelForm):
    class Meta :
        model =  Stock
        fields = ['ticker']