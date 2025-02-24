from django.db import models
from rest_framework.exceptions import ValidationError

NULLABLE = {"blank": True, "null": True}


class Supplier(models.Model):
    """Модель поставщика"""

    PROVIDER_TYPES = (
        ("factory", "Завод"),
        ("retail_network", "Розничная сеть"),
        ("Individual_entrepreneur", "Индивидуальный предприниматель"),
    )

    name = models.CharField(max_length=250, verbose_name="Название поставщика")
    provider = models.ForeignKey(
        "self", **NULLABLE, on_delete=models.SET_NULL, verbose_name="Поставщик"
    )
    provider_type = models.CharField(
        max_length=40, choices=PROVIDER_TYPES, verbose_name="Тип поставщика"
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        **NULLABLE,
        default=0,
        verbose_name="Задолжность перед поставщиком",
    )
    creation_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    level = models.IntegerField(default=1, verbose_name="Уровень в иерархии")

    def __str__(self):
        return f"{self.name} {self.provider_type} {self.level}"

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ("name",)

    # def clean(self):
    #     """Валидация данных для модели поставщика"""
    #
    #     if self.provider and self.provider == self:
    #         raise ValidationError(
    #             "Нельзя ссылаться на самого себя в качестве поставщика"
    #         )
    #     if self.provider:
    #         if self.level == 0 and self.provider is not None:
    #             raise ValidationError("Завод не может иметь поставщика")
    #         if self.level == 1 and self.provider.level == 2:
    #             raise ValidationError("Розничная сеть не может иметь поставщика ИП")
    #         if self.level == 2 and self.provider.level != 2:
    #             raise ValidationError("ИП не может быть поставщиком для другого ИП")


class Product(models.Model):
    """Модель продукта"""

    title = models.CharField(max_length=250, verbose_name="Название")
    model = models.CharField(max_length=250, **NULLABLE, verbose_name="Модель")
    release_date = models.DateTimeField(**NULLABLE, verbose_name="Дата выхода на рынок")
    provider = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, **NULLABLE, verbose_name="Поставщик"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("title",)


class Contact(models.Model):
    """Модель контакта"""

    email = models.EmailField(max_length=80, verbose_name="Email")
    country = models.CharField(max_length=200, verbose_name="Страна")
    city = models.CharField(max_length=150, verbose_name="Город")
    street = models.CharField(max_length=150, verbose_name="Улица")
    house_number = models.PositiveIntegerField(**NULLABLE, verbose_name="Номер дома")
    provider = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, **NULLABLE, verbose_name="Поставщик"
    )

    def __str__(self):
        return f"{self.email} {self.city} {self.country}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = (
            "city",
            "country",
        )
