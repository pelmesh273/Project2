# Generated by Django 3.2 on 2023-12-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Heat_Life', '0016_auto_20231208_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='coop',
            name='adress',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
