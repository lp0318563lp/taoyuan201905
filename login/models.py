from django.db import models

# Create your models here.
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    username = forms.EmailField(label="信箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="確認密碼", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label = "暱稱", max_length=128, widget = forms.TextInput(attrs={'class':'form-control'}))
    
