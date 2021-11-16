from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ChoiceSerializer, QuestionSerializer, LaptopSerializer

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


class ChoiceListAPI(APIView):
    def get(self, request):
        queryset = Choice.objects.all()
        print(queryset)
        serializer = ChoiceSerializer(queryset, many=True)
        return Response(serializer.data)


class QuestionListAPI(APIView):
    def get(self, request):
        queryset = Question.objects.all()
        print(queryset)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)


class LaptopListAPI(APIView):
    def get(self, request):
        queryset = Laptop.objects.all()
        print(queryset)
        serializer = LaptopSerializer(queryset, many=True)
        return Response(serializer.data)
