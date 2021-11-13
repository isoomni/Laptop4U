from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from .models import Question, Laptop, Choice


def index(request):
    laptops = Laptop.objects.all()

    context = {
        'laptops': laptops,
    }

    return render(request, 'main/index.html', context=context)
