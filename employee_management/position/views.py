from django.shortcuts import render

# Create your views here.

def position(request):
    return render(request,"position.html")