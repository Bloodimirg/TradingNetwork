from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Supplier, Product


def clear_debt(modeladmin, request, queryset):
    """
    Action для очищения задолженности перед поставщиком у выбранных объектов.
    """
    queryset.update(debt=0.00)


clear_debt.short_description = "Снять задолженность"


class ProductAdmin(admin.ModelAdmin):
    """Админка продукта"""

    def supplier_link(self, obj):
        return mark_safe(
            f'<a href="/admin/net/supplier/{obj.supplier.id}/">{obj.supplier}</a>'
        )

    supplier_link.short_description = "Поставщик"

    list_display = ["name", "product_model", "supplier_link"]


admin.site.register(Product, ProductAdmin)


class SupplierAdmin(admin.ModelAdmin):
    """Админка поставщиков"""

    list_display = ["name", "email", "country", "city", "debt", "created_at"]
    list_filter = ["city"]
    actions = [clear_debt]


admin.site.register(Supplier, SupplierAdmin)
