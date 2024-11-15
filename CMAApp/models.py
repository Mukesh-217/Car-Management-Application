from django.db import models
from django.contrib.auth.models import User
from django.forms import modelformset_factory
# Create your models here.

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "admin_table"

class JoinUs(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, unique=True)
    contact = models.BigIntegerField(blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    confirm_password = models.CharField(max_length=50, blank=False)  # Added confirm password
    joiningtime = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "joinus_table"



#demo



class Product(models.Model):
    id=models.AutoField(primary_key=True)
    category_choices = (("Home", "Home"), ("Jewelry", "Jewelry"), ("Electronics", "Electronics"), ("Clothes","Clothers"),("Others","Others"))
    category = models.CharField(max_length=100, blank=False,choices=category_choices)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200,blank=False)
    price = models.PositiveIntegerField(blank=False)
    image = models.FileField(blank=False,upload_to="productimages")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product_table"

class Car(models.Model):
    id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200,blank=False)
    owner = models.CharField(max_length=100, blank=False)
    price = models.PositiveIntegerField(blank=False)
    image = models.FileField(blank=False,upload_to="carimages")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "car_table"