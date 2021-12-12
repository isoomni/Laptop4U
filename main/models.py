from django.db import models



#Laptop 테이블의 fields(테이블의 열) 정의
class Laptop(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField(default=0, null=True)  # 몇 명이 해당 랩탑에 해당하는 것을 선택했는가
    laptop_store_url = models.URLField(null=True)
    laptop_fee_url = models.URLField(null=True)
    laptop_img = models.URLField(null=True)
    cpu_name = models.CharField(max_length=45, null=True)
    cpu_level = models.IntegerField(default=1)
    weight = models.FloatField(null=True)
    ram = models.IntegerField(default=0, null=True)
    battery = models.FloatField(null=True)
    display = models.FloatField(null=True)
    storage_space = models.IntegerField(null=True)
    os_type = models.CharField(max_length=1, default='W')
    touch = models.CharField(max_length=1, default='N')
    first_price = models.IntegerField(null=True)
    sales_price = models.IntegerField(null=True)
    pd_charge = models.CharField(max_length=1, default='N')
    review = models.FloatField(null=True)
    final_price = models.IntegerField(null=True)
    card_discount = models.CharField(max_length=10, default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=1, default='Y')

    def __str__(self):
        return self.name

#Question 테이블의 fields(테이블의 열) 정의
class Question(models.Model):
    question_contents = models.CharField(max_length=45, null=True)
    question_describe = models.CharField(max_length=45, null=True)
    question_img = models.URLField(null=True)
    question_type = models.CharField(max_length=45, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    status = models.CharField(max_length=1, default='Y', null=True)

    def __str__(self):
        return str(self.question_contents)

#Choice 테이블의 fields(테이블의 열) 정의
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_contents = models.CharField(max_length=45, null=True)
    choice_weight = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=1, default='Y')

    def __str__(self):
        return self.choice_contents
