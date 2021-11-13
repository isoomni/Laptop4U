from django.contrib import admin

# Register your models here.
from .models import Laptop, Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_contents']})
    ]
    inlines = [ChoiceInline]


admin.site.register(Laptop)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
