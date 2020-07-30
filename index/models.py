from django.db import models

# Create your models here.
class food(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    hotel_name=models.CharField(max_length=100)
    rating=models.IntegerField()
    location=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)

class Popular_food(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    hotel_name=models.CharField(max_length=100)
    rating=models.FloatField()
    location=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)
    desc=models.TextField()
