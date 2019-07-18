from django.shortcuts import render
from first_app.forms import LoginForm

# Create your views here.
def login_page_view(request):
    form = LoginForm()

    if request.method =="POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return tables_view(request)
        else:
            print("Error Form Invalid")
    return render(request,'first_app/index.html',{'form':form})



def index(request):
    return render(request,'first_app/index.html')
