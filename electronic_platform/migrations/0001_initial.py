# Generated by Django 5.1.6 on 2025-02-23 06:08

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
                (
                    "name",
                    models.CharField(
                        max_length=250, verbose_name="Название поставщика"
                    ),
                ),
                (
                    "supplier_type",
                    models.CharField(
                        choices=[
                            ("factory", "Завод"),
                            ("retail_network", "Розничная сеть"),
                            (
                                "Individual_entrepreneur",
                                "Индивидуальный предприниматель",
                            ),
                        ],
                        max_length=40,
                        verbose_name="Тип поставщика",
                    ),
                ),
                (
                    "debt",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                        verbose_name="Задолжность перед поставщиком",
                    ),
                ),
                (
                    "creation_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="electronic_platform.supplier",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Поставщик",
                "verbose_name_plural": "Поставщики",
                "ordering": ("name",),
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
                ("title", models.CharField(max_length=250, verbose_name="Название")),
                (
                    "model",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="Модель"
                    ),
                ),
                (
                    "release_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата выхода на рынок"
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="electronic_platform.supplier",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("email", models.EmailField(max_length=80, verbose_name="Email")),
                ("country", models.CharField(max_length=200, verbose_name="Страна")),
                ("city", models.CharField(max_length=150, verbose_name="Город")),
                ("street", models.CharField(max_length=150, verbose_name="Улица")),
                (
                    "house_number",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Номер дома"
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="electronic_platform.supplier",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
                "ordering": ("city", "country"),
            },
        ),
    ]
