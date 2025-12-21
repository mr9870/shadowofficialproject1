from django.shortcuts import render
from .models import Tool

def home(request):
    tools = Tool.objects.all()
    return render(request, 'core/home.html', {'tools': tools})

from django.shortcuts import render
from .models import Tool, AdminProfile # AdminProfile yahan zaroori hai

def home(request):
    tools = Tool.objects.all()
    # Pehla profile fetch karne ke liye (kyunki aap ek hi admin hain)
    profile = AdminProfile.objects.first() 
    return render(request, 'core/home.html', {'tools': tools, 'profile': profile})