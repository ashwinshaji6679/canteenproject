from django.db import models

# Create your models here.

class ulogin1(models.Model):
    key= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    password= models.CharField(max_length=60)
    college_id= models.CharField(max_length=60)
    email= models.CharField(max_length=60)
class food(models.Model):
    key= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    price = models.CharField(max_length=60)
    plate= models.CharField(max_length=60)

class dayfood1(models.Model):
    key= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    price = models.CharField(max_length=60)
    plate= models.CharField(max_length=60)
    date= models.CharField(max_length=60)
    time= models.CharField(max_length=60)
class cart(models.Model):
    key= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    price = models.CharField(max_length=60)
    quantity= models.CharField(max_length=60)
    date= models.CharField(max_length=60)
    time= models.CharField(max_length=60)
    item= models.CharField(max_length=60)
    expire= models.CharField(max_length=60)

class bill5(models.Model):
    key= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    price = models.CharField(max_length=60)
    item = models.CharField(max_length=60)
    quan = models.CharField(max_length=60)
    ids = models.CharField(max_length=60)
    time= models.CharField(max_length=60)
    date=models.CharField(max_length=60)
    status=models.CharField(max_length=60)
    qprice=models.CharField(max_length=60)
    use=models.CharField(max_length=60)

class stats1(models.Model):
    key=models.IntegerField(primary_key=True)
    date=models.CharField(max_length=60)
    amount=models.CharField(max_length=60)
   
   

   