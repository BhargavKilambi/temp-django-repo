from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Pharma(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    phone = PhoneNumberField()
    address = models.TextField(max_length=300)

    def __str__(self):
        return self.title


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100,default='')
    price = models.DecimalField(max_digits=7,decimal_places=2)
    des = models.TextField(max_length=400)
    pharma = models.ManyToManyField(Pharma,related_name='pharma')

    def __str__(self):
        return self.name
