import django_filters

from .models import Laptop

class LaptopFilter(django_filters.FilterSet):
    
    # class Meta:
    #     model = Laptop
    #     fields = [
    #         'cpu_level',
    #         'weight',
    #         'ram',
    #         'battery',
    #         'display',
    #         'storage_space',
    #         'os_type',
    #         'touch',
    #         'final_price',
    #         'pd_charge',
    #     ]
    
    class cpu:
        model = Laptop
        fields = ['cpu_level',]
        
    class weight:
        model = Laptop
        fields = ['weight',]