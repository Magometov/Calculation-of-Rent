from django.db import models

from src.apps.core.models.admins.ApartmentModelAdmin import ApartmentAdmin


class Apartment(models.Model):
    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
        default_related_name = "apartments"

    ModelAdmin = ApartmentAdmin

    house = models.ForeignKey(
        "core.House",
        on_delete=models.CASCADE,
        verbose_name="Дом",
    )
    number = models.PositiveSmallIntegerField(verbose_name="Номер квартиры")
    square = models.PositiveIntegerField(verbose_name="Площадь")

    def __str__(self):
        return f"{self.house} {self.number}"
