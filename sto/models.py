from django.db import models
from django.contrib.auth.models import User

class Sto(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sto')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sto_logo/', blank=False)

    def __str__(self):
        return self.name

class Services(models.Model):
    service_type = models.CharField(max_length=30)

    def __str__(self):
        return self.service_type

class StoService(models.Model):
    sto = models.ForeignKey(Sto)
    name = models.CharField(max_length=100)
    service_type = models.ForeignKey(Services)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services_images/', blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
