# Generated by Django 5.0.6 on 2024-06-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Добавить в меню или нет?'),
        ),
    ]