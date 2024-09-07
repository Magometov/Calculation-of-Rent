from django.db import models

from src.apps.core.const import CityChoices
from src.apps.core.models.admins.HouseModelAdmin import HouseAdmin


class House(models.Model):
    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"

    ModelAdmin = HouseAdmin

    city = models.PositiveSmallIntegerField(
        verbose_name="Город",
        choices=CityChoices,
        default=CityChoices.spb,
    )
    district = models.CharField(verbose_name="Район", max_length=100)
    address = models.CharField(verbose_name="Адрес", max_length=100)

    def __str__(self):
        return f"{self.get_city_display()} {self.address}"
