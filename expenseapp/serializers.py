from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        #fields = '__all__'
        fields = ['id', 'user', 'title', 'amount', 'date', 'description', 'category']
        extra_kwargs = {
            'user': {'read_only': True}
        }