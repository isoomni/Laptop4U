from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 동적인 값들을 가져와야 합니다.
from .models import Question, Laptop, Choice

def index(request):
    
    laptops = Laptop.objects.all()

    context = {'laptops': laptops}
    
    return render(request, 'main/index.html', context=context)

def details(request):
    questions = Question.objects.all()
    
    context = {'questions': questions}
    
    return render(request, 'main/details.html', context=context)



def result(request):
    
    results = Laptop.objects.filter(cpu_level="1")

    
    return render(request, 'main/results.html', context=context)
