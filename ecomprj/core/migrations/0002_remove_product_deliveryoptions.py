# Generated by Django 4.2.2 on 2024-02-13 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='deliveryOptions',
        ),
    ]