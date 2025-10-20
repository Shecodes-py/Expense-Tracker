from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):  
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors) 
        #serializer.save(user=self.request.user)

class ExpenseListDeleteView(generics.DestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)