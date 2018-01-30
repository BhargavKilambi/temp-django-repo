from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Category(models.Model):
    c_name = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category,related_name='category')
    qualification = models.CharField(max_length=150)
    des = models.TextField(max_length=200)
    phone = PhoneNumberField()

    def __str__(self):
        return self.name
