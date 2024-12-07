from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """Получение пары токенов access/refresh"""

    serializer_class = CustomTokenObtainPairSerializer
