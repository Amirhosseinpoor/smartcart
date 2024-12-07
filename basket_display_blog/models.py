from django.db import models

# Create your models here.
class BasketInfo(models.Model):
    basket_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    customer_company = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    goods_id = models.CharField(max_length=255)
    goods_name = models.CharField(max_length=255)
    date = models.DateField()
    health = models.BooleanField()