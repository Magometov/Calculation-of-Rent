from django.db import models

from src.apps.core.models.admins.WaterMeterModelAdmin import WaterMeterAdmin


class WaterMeter(models.Model):
    class Meta:
        verbose_name = "Счетчик воды"
        verbose_name_plural = "Счетчики воды"
        default_related_name = "water_meters"

    ModelAdmin = WaterMeterAdmin

    apartment = models.ForeignKey(
        "core.Apartment",
        on_delete=models.CASCADE,
        verbose_name="Квартира",
    )
