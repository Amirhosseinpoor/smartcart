from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models


class BasketInfoModel(AbstractUser):
    basket_id = models.BigIntegerField(primary_key=True)
    basket_name = models.CharField(max_length=255)
    basket_health = models.BooleanField(default=True)
    basket_version = models.IntegerField(default=1)
    customer_company_id = models.BigIntegerField(blank=True, null=True)
    customer_company_name = models.CharField(max_length=255)
    customer_company_number = models.BigIntegerField(blank=True, null=True)
    customer_company_email = models.EmailField(max_length=255)
    goods_id = models.BigIntegerField(blank=True, null=True)
    goods_name = models.CharField(max_length=255)
    goods_features = models.CharField(max_length=255)
    date = models.DateField(default=date.today)

    def save(self, *args, **kwargs):
        # مقداردهی خودکار basket_id اگر مقدار داده نشده باشد
        if not self.basket_id:
            max_id = BasketInfoModel.objects.aggregate(models.Max('basket_id'))['basket_id__max'] or 0
            self.basket_id = max_id + 1
        super().save(*args, **kwargs)
