from django.urls import path, include
from .views import ExpenseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')
# we are already dealing with the django framework, it has inbuilt API routes
# This means your endpoints will start with /expenses/

urlpatterns = [
    path('', include(router.urls) )
]
