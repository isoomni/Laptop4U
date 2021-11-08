from django.shortcuts import render

# Create your views here.
from .models import Question, Laptop, Choice

def index(request):
    laptops = Laptop.objects.all()
    
    context = {
        'laptops': laptops,
    }
    
    return render(request, 'index.html', context=context)