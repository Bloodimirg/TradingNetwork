from django.urls import path
from rest_framework.permissions import AllowAny
from users.apps import UsersConfig
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import CustomTokenObtainPairView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login",),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
