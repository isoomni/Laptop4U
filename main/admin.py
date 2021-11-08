from django.contrib import admin

# Register your models here.
from .models import Laptop, Question, Choice

admin.site.register(Laptop)
admin.site.register(Question)
admin.site.register(Choice)