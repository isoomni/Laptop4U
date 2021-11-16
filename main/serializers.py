from rest_framework import serializers
from .models import Choice, Question, Laptop


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice        # Choice 모델 사용
        fields = '__all__'            # 모든 필드 포함


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question        # Question 모델 사용
        fields = '__all__'            # 모든 필드 포함


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop        # Laptop 모델 사용
        fields = '__all__'            # 모든 필드 포함
