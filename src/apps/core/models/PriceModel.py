from django.db import models

from src.apps.core.models.admins.PriceModelAdmin import PriceAdmin


class Price(models.Model):
    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"
        default_related_name = "prices"

    ModelAdmin = PriceAdmin

    house = models.ForeignKey(
        "core.House",
        on_delete=models.CASCADE,
        verbose_name="Дом",
    )
    cost = models.PositiveSmallIntegerField(verbose_name="Цена")
