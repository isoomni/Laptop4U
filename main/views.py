from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
#from .serializers import ChoiceSerializer, QuestionSerializer, LaptopSerializer
from django.db.models import Q
from .filters import LaptopFilter
from django.core.paginator import Paginator

# Create your views here.
# 동적인 값들을 가져와야 합니다.
from .models import Question, Laptop, Choice, Answer


def index(request):
    
    rank = Laptop.objects.order_by('-count')

    laptops = Laptop.objects.all()
    # counts = Laptop.objects.count()

    context = {'laptops': laptops, 'rank':rank}

    return render(request, 'main/index.html', context=context)


def details(request):
    questions = Question.objects.all()

    context = {'questions': questions}

    return render(request, 'main/details.html', context=context)



def results(request):
    q0_choice = request.POST.get("question0")
    q1_choice = request.POST.get("question1")
    q2_choice = request.POST.get("question2")
    q3_choice = request.POST.get("question3")
    q4_choice = request.POST.get("question4")
    q5_choice = request.POST.get("question5")   
    q6_choice = request.POST.get("question6")
    q7_choice = request.POST.get("question7")
    q8_choice = request.POST.get("question8")
     
    q = Q()
    
    if q0_choice == '1':
        q.add(Q(display__gte=15), q.AND)
    else:
        q.add(Q(display__lt=15), q.AND)
    
    if q1_choice == '3':
        q.add(Q(cpu_level=1), q.AND)
    else:
        pass
    
    if q2_choice == '5':
        q.add(Q(ram__gte=16), q.AND)
    else:
        pass
        
    if q3_choice == '7':
        q.add(Q(os_type='I'), q.AND)
    else:
        q.add(Q(os_type='W'), q.AND)
    
    if q4_choice == '10':
        q.add(Q(pd_charge='C'), q.AND)
    else:
        q.add(Q(pd_charge='N'), q.AND)
        
    if q5_choice == '12':
        q.add(Q(touch='Y'), q.AND)
    else:
        q.add(Q(touch='N'), q.AND)
        
    if q6_choice == '14' or q6_choice == '15':
        q.add(Q(cpu_level = 1), q.AND)
    else:
        pass
    
    if q7_choice == '19':
        q.add(Q(final_price__lte=1000000), q.AND)
    elif q7_choice == '20':
        q.add(Q(final_price__lte=1500000), q.AND)
    
    if q8_choice == '22':
        q.add(Q(weight__lte=1.3), q.AND)
    elif q8_choice == '23':
        q.add(Q(weight__lte=1.5), q.AND)
    
    
    results = Laptop.objects.filter(q).order_by('final_price') #상위3개
    
    if len(results) == 0:
        return render(request, 'main/no_results.html',{"results" : results})   
        
    result_list = []
    similar_list = []
    similar_len = 0

    
        # 상위1:
    if len(results) > 0:
        result_list.append([results[0].name, results[0].laptop_img, results[0].cpu_level, results[0].final_price, 
                            results[0].weight, results[0].ram, results[0].battery, 
                            results[0].display, results[0].storage_space, results[0].os_type, results[0].touch, 
                            results[0].review, results[0].laptop_fee_url,results[0].cpu_name ,results[0].card_discount, results[0].first_price])

    if len(results)>1:
        similar_len += 1
        similar_list.append([results[1].name, results[1].laptop_img, results[1].cpu_level, results[1].final_price, 
                            results[1].weight, results[1].ram, results[1].battery, 
                            results[1].display, results[1].storage_space, results[1].os_type, results[1].touch, 
                            results[1].review, results[1].laptop_fee_url,results[1].cpu_name ,results[1].card_discount, results[1].first_price])

    if len(results)>2:
        similar_len += 1
        similar_list.append([results[2].name, results[2].laptop_img, results[2].cpu_level, results[2].final_price, 
                            results[2].weight, results[2].ram, results[2].battery, 
                            results[2].display, results[2].storage_space, results[2].os_type, results[2].touch, 
                            results[2].review, results[2].laptop_fee_url, results[2].cpu_name ,results[2].card_discount, results[2].first_price])

    print(result_list)
        # Laptop.count += 1
    '''
    selected_choice = Answer.answer_set.get(pk=results[0].id)
    selected_choice.result_count += 1
    selected_choice.save()
     '''

    laptopcount = Laptop.objects.get(id=results[0].id) 
    laptopcount.count = laptopcount.count +1
    laptopcount.save()
    
    
    
    return render(request, 'main/results.html',{"result_list" : result_list, 
                                                "similar_list" : similar_list, "similar_len" : similar_len})                            

def all_laptop(request):
    laptops = Laptop.objects.all()

    context = {'laptops': laptops}

    return render(request, 'main/all_laptop.html', context=context)
