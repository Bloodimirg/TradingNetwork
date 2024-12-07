from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsActiveUser
from .models import Supplier, Product
from .serializers import SupplierSerializer, ProductSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    """
    Получение списка поставщиков и создание нового поставщика.
    """

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]
    filterset_fields = ["country"]

    def get_queryset(self):
        queryset = Supplier.objects.all()
        country = self.request.query_params.get("country", None)
        if country:
            queryset = queryset.filter(country=country)
        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    """
    Получение, обновление или удаление данных одного продукта.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ["name"]
