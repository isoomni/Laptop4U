from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
#from .serializers import ChoiceSerializer, QuestionSerializer, LaptopSerializer

# Create your views here.
# 동적인 값들을 가져와야 합니다.
from .models import Question, Laptop, Choice


def index(request):

    laptops = Laptop.objects.all()
    counts = Laptop.objects.count()

    context = {'laptops': laptops}

    return render(request, 'main/index.html', context=context)


def details(request):
    questions = Question.objects.all()

    context = {'questions': questions}

    return render(request, 'main/details.html', context=context)


def result(request):
    
    # Question1
    if (선택지1):
        results = Laptop.objects.filter(display>=15)
    else:
        results = Laptop.objects.filter(display<15)
        
    
    results = Laptop.objects.filter(cpu_level="1")
    
#     display               = request.GET.getlist('display', None)
#     cpu_level              = request.GET.getlist('cpu_level', None)
#     price_upper_range  = request.GET.get('PriceUpper', 1000000)
#     price_lower_range  = request.GET.get('PriceLower', 0)

#     q=Q()
#     if category:
#         q &= Q(category_id = category)
#     if color:
#         q &= Q(color_name__in = color)
#     if size:
#         q &= Q(size__name__in = size)

#     q &= Q(price__range = (price_lower_range,price_upper_range))
    
    
    

    return render(request, 'main/results.html', context=context)


# class LaptopListAPI(APIView):
#     def get(self, request):
#         # queryset = Laptop.objects.all()
        
#         laptops = Laptop.objects.all()
        
#         print(queryset)
#         serializer = LaptopSerializer(laptops, many=True)
#         return Response(serializer.data)


# class ChoiceListAPI(APIView):
#     def get(self, request):
#         queryset = Choice.objects.all()
#         print(queryset)
#         serializer = ChoiceSerializer(queryset, many=True)
#         return Response(serializer.data)


# class QuestionListAPI(APIView):
#     def get(self, request):
#         queryset = Question.objects.all()
#         print(queryset)
#         serializer = QuestionSerializer(queryset, many=True)
#         return Response(serializer.data)

# class QNAListAPI(APIView):
#     def get(self, request):
#         queryset = Question.objects.all()
#         print(queryset)
#         serializer = QNASerializer(queryset, many=True)
#         return Response(serializer.data)