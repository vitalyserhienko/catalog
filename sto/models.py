from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Sto(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sto')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sto_logo/', blank=False)

    def __str__(self):
        return self.name
