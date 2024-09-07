from django.db import models

from src.apps.core.models.admins.WaterMeterReadingModelAdmin import (
    WaterMeterReadingAdmin,
)


class WaterMeterReading(models.Model):
    class Meta:
        verbose_name = "Показания счетчика"
        verbose_name_plural = "Показании счетчика"
        default_related_name = "reading"
        unique_together = [["meter", "date"]]

    ModelAdmin = WaterMeterReadingAdmin

    meter = models.ForeignKey(
        "core.WaterMeter",
        on_delete=models.CASCADE,
        verbose_name="Счетчик",
    )
    date = models.DateField(verbose_name="Дата")
    reading = models.PositiveSmallIntegerField("Показания")
