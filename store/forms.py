from django import forms
from django.db import models
from django.db.models import fields
from .models import *

class inputTypeProduct(forms.ModelForm):
    class Meta:
        model = TypeProduct
        fields =['name', 'desc']

