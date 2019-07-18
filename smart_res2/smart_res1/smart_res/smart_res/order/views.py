from django.shortcuts import render,redirect
from order.forms import LoginForm, OrderForm
from order.decorators import check_form_submitted
from order.models import FoodItem, Order, FoodClass
# Create your views here.

def index(request):
    form = LoginForm()

    if request.method =="POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            request.session['form_submitted'] = True
            return redirect('type/')
        else:
            print("Error! Invalid Form.")
    return render(request,'order/index.html',{'form':form})


@check_form_submitted
def food_type_view(request):
    food_types = FoodClass.objects.all()
    food_dict = {'food_records': food_types}
    return render(request,'order/food_type.html', context=food_dict)

@check_form_submitted
def veg_food_view(request):
    veg_types = FoodItem.objects.filter(food_super_class__class_name__contains="veg")
    veg_dict = {'veg_records': veg_types}
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('type/')
        else:
            print("Error")
    return render(request,'order/veg_food.html', {'form':form, 'veg_records':veg_dict})

@check_form_submitted
def nonveg_food_view(request):
    return render(request,'order/nonveg_food.html')

@check_form_submitted
def drink_view(request):
    return render(request,'order/drinks.html')
