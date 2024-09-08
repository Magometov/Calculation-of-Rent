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
    serial_number = models.CharField(verbose_name="Серийный номер", max_length=50)

    def __str__(self):
        return f"{self.serial_number} | {self.apartment}"
