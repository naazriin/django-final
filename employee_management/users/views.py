from django.shortcuts import render
from users.forms import RegisterForm
# Create your views here.


def login(request):
    return render(request, 'login.html')

def register(request):
    form = RegisterForm
    context = {
        'form': form
        
    }
    return render(request, 'register.html', context)