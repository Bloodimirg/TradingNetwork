from rest_framework import serializers
from .models import Supplier, Product


class SupplierSerializer(serializers.ModelSerializer):

    def validate(self, data):
        # Проверяем, не пытались ли изменить задолженность
        if "debt" in data:
            raise serializers.ValidationError(
                {"debt": "Невозможно изменить задолженность перед поставщиком."}
            )
        return data

    class Meta:
        model = Supplier
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
