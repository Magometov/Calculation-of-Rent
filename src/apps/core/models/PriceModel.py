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

    price_for_water_supply = models.PositiveSmallIntegerField(verbose_name="Цена за водоснабжение", default=0)
    price_for_area = models.PositiveSmallIntegerField(verbose_name="Цена за площадь", default=0)

    def __str__(self):
        return f"{self.house}"
