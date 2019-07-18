from django.shortcuts import render,redirect
from order.forms import LoginForm
from order.decorators import check_form_submitted
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
    return render(request,'order/food_type.html')

@check_form_submitted
def veg_food_view(request):
    return render(request,'order/veg_food.html')

@check_form_submitted
def nonveg_food_view(request):
    return render(request,'order/nonveg_food.html')

@check_form_submitted
def drink_view(request):
    return render(request,'order/drinks.html')
