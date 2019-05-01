from django.db import models

# Create your models here.
class member(models.Model):
     memberId = models.AutoField(primary_key=True)
     memberAccount = models.CharField(max_length = 70)
     memberEmail = models.EmailField(max_length=70)
     memberPassword = models.CharField(max_length=30)
     memberName = models.CharField(max_length=30)
     dailyConsum = models.IntegerField(max_length=10, null=True)
     