from django.urls import path, include
from . import views
#from rest_framework.routers import DefaultRouter

#router = DefaultRouter()   # For Viewsets
#router.register(r'expenses', views.ExpenseListCreateView, basename='expense')

urlpatterns = [
    #path('', include(router.urls)),
    path('expenses/', views.ExpenseListCreateView.as_view(), name='expense-list-create'), # For ApiViews
    path('expenses/delete/', views.ExpenseListCreateView.as_view(), name='delete-expenses'),
]