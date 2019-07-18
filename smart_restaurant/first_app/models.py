from django.db import models

# Create your models here.
class LoginModel(models.Model):
    username = models.CharField(max_length=128)
    
