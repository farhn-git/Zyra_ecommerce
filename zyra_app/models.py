from django.db import models

# Create your models here.
class Collection(models.Model):
    name=models.CharField(max_length=200)

class Products(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image1=models.ImageField(upload_to='images/')
    image2=models.ImageField(upload_to='images/')
    COLLECTION=models.ForeignKey(Collection, on_delete=models.CASCADE)

class Login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=20)

class Customer(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.TextField(max_length=200)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()

class Order(models.Model):
    date=models.DateField()
    price=models.IntegerField()
    PRODUCT=models.ForeignKey(Products,on_delete=models.CASCADE)
    COLLECTION=models.ForeignKey(Collection,on_delete=models.CASCADE)
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Cart(models.Model):
    PRODUCT=models.ForeignKey(Products,on_delete=models.CASCADE)
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField()

class Favorites(models.Model):
    PRODUCT=models.ForeignKey(Products,on_delete=models.CASCADE)
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE)

