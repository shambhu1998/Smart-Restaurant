from django.db import models
from django.conf import settings

class LoginModel(models.Model):
    username = models.CharField(max_length=264)
    Table_number = models.ValueRange(start=1, end=10)

    def __str__(self):
        return "%s" % self.username


class FoodClass(models.Model):
    class_name = models.CharField(max_length=264)

    def __str__(self):
        return "%s" % self.class_name


class FoodItem(models.Model):
    food_name = models.CharField(max_length=264)
    price = models.PositiveIntegerField()
    food_description = models.TextField()
    food_super_class = models.ForeignKey(FoodClass, on_delete=None)
    food_image = models.ImageField(upload_to=settings.IMAGE_DIR, blank=True)

    def __str__(self):
        return "%s" % self.food_name


class Order(models.Model):
    order_id = models.ForeignKey(LoginModel, on_delete=models.CASCADE)
    order_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    order_quantity = models.IntegerField(default='1')

    def __str__(self):
        return "%s %s" % (self.order_item_id, self.order_item)