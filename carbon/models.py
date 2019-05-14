from django.db import models
from django import forms
# Create your models here.

class carbon(models.Model):
    carbonId = models.AutoField(primary_key = True)
    carbonClass = models.CharField(max_length = 10)
    carbonName = models.CharField(max_length = 20)
    carbonCoporation = models.CharField(max_length = 20)
    carbonFootprint = models.CharField(max_length = 10)
    carbonUnit = models.CharField(max_length = 15)

class submitCarbonForm(forms.Form):
    quantity = forms.IntegerField(label='輸入購買數量', widget=forms.NumberInput,max_value=None,required=False)