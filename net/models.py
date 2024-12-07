from django.db import models
from django.db.models import SET_NULL
from users.models import NULLABLE
from .utils import save_supplier


class Supplier(models.Model):
    """Модель поставщика"""

    ZERO = 0
    FIRST = 1
    SECOND = 2
    LEVEL = [
        (ZERO, "Завод"),
        (FIRST, "Розничная сеть"),
        (SECOND, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.EmailField(max_length=100, verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.PositiveIntegerField(verbose_name="Номер дома")

    level = models.PositiveSmallIntegerField(choices=LEVEL, verbose_name="Уровень сети")
    supplier = models.ForeignKey("self",  on_delete=SET_NULL, related_name="suppliers", verbose_name="Поставщик", **NULLABLE)
    debt = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Задолженность перед поставщиком руб.")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def save(self, *args, **kwargs):
        # Вызываем переопределенную функцию для вычисления уровня и сохранения данных
        save_supplier(self, *args, **kwargs)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

class Product(models.Model):
    """Модель продукта"""

    name = models.CharField(max_length=250, verbose_name="Название продукта")
    product_model = models.CharField(max_length=250, verbose_name="Модель продукта")
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок")
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, verbose_name="Поставщик"
    )


    def __str__(self):
        return f"{self.name} ({self.product_model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

