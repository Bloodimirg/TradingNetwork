# Generated by Django 5.1.4 on 2024-12-07 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Имя")),
                ("email", models.EmailField(max_length=100, verbose_name="Email")),
                ("country", models.CharField(max_length=100, verbose_name="Страна")),
                ("city", models.CharField(max_length=100, verbose_name="Город")),
                ("street", models.CharField(max_length=100, verbose_name="Улица")),
                (
                    "house_number",
                    models.PositiveIntegerField(verbose_name="Номер дома"),
                ),
                (
                    "level",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Завод"),
                            (1, "Розничная сеть"),
                            (2, "Индивидуальный предприниматель"),
                        ],
                        verbose_name="Уровень сети",
                    ),
                ),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=15,
                        verbose_name="Задолженность перед поставщиком руб.",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="suppliers",
                        to="net.supplier",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Звено сети",
                "verbose_name_plural": "Звенья сети",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=250, verbose_name="Название продукта"),
                ),
                (
                    "product_model",
                    models.CharField(max_length=250, verbose_name="Модель продукта"),
                ),
                (
                    "release_date",
                    models.DateField(verbose_name="Дата выхода продукта на рынок"),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="net.supplier",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
