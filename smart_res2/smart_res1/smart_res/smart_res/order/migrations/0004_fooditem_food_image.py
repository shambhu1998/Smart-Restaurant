# Generated by Django 2.1 on 2018-11-23 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_loginmodel_table_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='food_image',
            field=models.ImageField(blank=True, upload_to='C:\\Users\\Light\\Desktop\\smart_res\\smart_res\\photo_path'),
        ),
    ]
