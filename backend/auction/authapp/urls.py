from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, re_path

urlpatterns = [
    path("login", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]