# Generated by Django 2.0.5 on 2018-11-23 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20181123_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='food_description',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='food_image',
        ),
    ]