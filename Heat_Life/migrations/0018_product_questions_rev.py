# Generated by Django 3.2 on 2023-12-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Heat_Life', '0017_coop_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Название', max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='static\\media\\img')),
                ('short_desc', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('full_desc', models.TextField(blank=True, verbose_name='Полное описание')),
                ('extra_desc', models.TextField(blank=True, verbose_name='Дополнительная информация')),
                ('tech_desc', models.TextField(blank=True, verbose_name='Технические характеристики')),
                ('language', models.CharField(default='EN', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Вопрос', max_length=200)),
                ('desc', models.TextField(blank=True, verbose_name='Ответ')),
                ('language', models.CharField(default='EN', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='rev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Заголовок', max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='static\\media\\img')),
                ('review', models.TextField(blank=True, verbose_name='Отзыв')),
                ('name', models.CharField(default='Имя', max_length=200)),
                ('language', models.CharField(default='EN', max_length=200)),
            ],
        ),
    ]
