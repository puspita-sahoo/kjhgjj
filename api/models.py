from django.db import models
from django.contrib.auth.models import User




class UserProfile(models.Model):
    USER_TYPE = (('1', 'Customer'),('2', 'Shoper'))
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(help_text=" User type (Customer, Shoper)", choices=USER_TYPE, default='1',max_length=20)
    full_name = models.CharField(max_length=255,null=True,blank=True)
    phone = models.BigIntegerField(null=True,blank=True)
    alternate_phone = models.BigIntegerField(null=True,blank=True)
    terms_condition_privacy = models.BooleanField(default=False)
    address = models.CharField(max_length=255,null=True,blank=True)
    street_name = models.CharField(max_length=255,null=True,blank=True)
    zipcode = models.CharField(max_length=30, null=True, blank=True )
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name




class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    categories = models.CharField(max_length=50, null=True)
    image = models.ImageField()
    reviews = models.CharField(max_length=100)
    categories = models.CharField(max_length=50, null=True)
    stock = models.CharField(max_length=100)

