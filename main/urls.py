from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('results/', views.results, name='results'),
    path('all-laptops/', views.all_laptop, name='all_laptop'),

]
