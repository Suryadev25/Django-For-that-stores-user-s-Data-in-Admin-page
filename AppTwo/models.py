from django.db import models

# Create your models here.
class User(models.Model):
    First_Name = models.CharField(max_length = 126)
    Last_Name = models.CharField(max_length = 126)
    Email = models.EmailField(max_length = 266,unique = True)
