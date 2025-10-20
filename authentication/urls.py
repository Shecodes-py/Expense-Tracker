from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 

urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="Register"),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh"),
    path('api-auth/', include('rest_framework.urls')),
]