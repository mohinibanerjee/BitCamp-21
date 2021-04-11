from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20 )
    username = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    volume = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    study_time = models.CharField(max_length=20)
    study_period = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)



