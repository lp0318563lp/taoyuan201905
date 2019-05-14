from django.db import models

# Create your models here.
class member(models.Model):
     memberId = models.AutoField(primary_key=True)
     memberEmail = models.EmailField(max_length=70)
     memberPassword = models.CharField(max_length=30)
     memberName = models.CharField(max_length=30)
     dailyConsum = models.FloatField(max_length=10, default=0.0)
     nowDay = models.DateField(null = True)
     lastWeekConsume = models.FloatField(max_length=10, default=0.0)
     laskWeek = models.DateField(null = True)