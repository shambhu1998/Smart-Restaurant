# Generated by Django 2.1 on 2018-11-23 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=264)),
                ('price', models.PositiveIntegerField()),
                ('food_description', models.TextField()),
                ('food_super_class', models.ForeignKey(on_delete=None, to='order.FoodClass')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.IntegerField(default='1')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.LoginModel')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.FoodItem')),
            ],
        ),
    ]
