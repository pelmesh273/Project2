# Generated by Django 3.2 on 2023-12-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Heat_Life', '0022_order_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='prod',
            field=models.CharField(default='default', max_length=200),
        ),
    ]
