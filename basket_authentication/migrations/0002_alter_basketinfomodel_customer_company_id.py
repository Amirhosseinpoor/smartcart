# Generated by Django 5.1.4 on 2024-12-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketinfomodel',
            name='customer_company_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
