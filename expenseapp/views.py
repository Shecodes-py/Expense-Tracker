from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Expense
from .serializers import ExpenseSerializer

# Create your views here.
class ExpenseViewSet(viewsets.ModelViewSet): 
    queryset = Expense.objects.all() 
    serializer_class = ExpenseSerializer

    
'''
class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)'''