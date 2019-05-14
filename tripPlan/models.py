from django.db import models

# Create your models here.
from django import forms


class tripPlanForm(forms.Form):
    SELVALUE = (
        ('台北市','01'),
        ('桃園市','02'),
    )
    sel_value = forms.CharField(max_length=10,widget=forms.widgets.Select(choices=SELVALUE))