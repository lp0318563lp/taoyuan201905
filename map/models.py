from django.db import models

# Create your models here.
from django import forms

class mapAttractions(models.Model):
    attractionsId = models.AutoField(max_length=30,primary_key = True)
    attractionsName = models.CharField(max_length=30)
    attractionsToldescribe = models.CharField(max_length=300)
    attractionsAddress = models.CharField(max_length=30)
    attractionsOpentime = models.CharField(max_length=30)
    attractionsPx = models.FloatField(max_length=30)
    attractionsPy = models.FloatField(max_length=30)
    attractionsParkinfo = models.CharField(max_length=30)
    attractionsTel = models.CharField(max_length=15)
    

class tripPlanForm(forms.Form):
    SELVALUE = (
        ('1','台北市'),
        ('2','桃園市'),
    )
    day = (
        ('1','1天'),
        ('2','2天'),
        ('3','3天'),
    )
    sel_value = forms.CharField(label='縣市',max_length=10,widget=forms.Select(choices=SELVALUE))
    sel_day = forms.CharField(label='天數',max_length=10,widget = forms.Select(choices=day))


