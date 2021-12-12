from django.contrib import admin
from .models import Laptop, Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None,               {'fields': ['question_contents']}),
        ('Question information', {'fields': ['question_describe','question_img','question_type', 'status']}),
    ]
    
    inlines = [ChoiceInline]

admin.site.register(Laptop)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
