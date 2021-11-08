from django.db import models

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)  # 몇 명이 해당 랩탑에 해당하는 것을 설정했는가
    
    def __str__(self):
        return self.name

class Question(models.Model):
    number = models.IntegerField(unique=True)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.number}. {self.content}'

class Choice(models.Model):
    content = models.CharField(max_length=100)   
    question = models.ForeignKey(to='main.Question', 
                                 on_delete=models.CASCADE)
    laptop = models.ForeignKey(to='main.Laptop', 
                               on_delete=models.CASCADE,
                              null=True)
    def __str__(self):
        return self.content