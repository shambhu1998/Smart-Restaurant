from django.conf.urls import url,include
from order import views

app_name = 'order'

urlpatterns = [
    url(r'^$',views.food_type_view,name='food_type_view'),
    url(r'^veg/',views.veg_food_view,name='veg_food'),
    url(r'^nonveg/',views.nonveg_food_view,name='nonveg_food'),
    url(r'^drinks/',views.drink_view,name='drinks'),
]
