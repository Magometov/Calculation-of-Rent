from django.db import models

from src.apps.core.const import MonthChoices
from src.apps.core.models.admins.WaterMeterReadingModelAdmin import (
    WaterMeterReadingAdmin,
)


class WaterMeterReading(models.Model):
    class Meta:
        verbose_name = "Показания счетчика"
        verbose_name_plural = "Показании счетчика"
        default_related_name = "reading"
        constraints = [
            models.UniqueConstraint(
                fields=["meter", "date"],
                name="%(app_label)s_%(class)s_unique_pair_of_meter_and_date",
                violation_error_message="На этот месяц показания счетчика уже записаны.",
            )
        ]

    ModelAdmin = WaterMeterReadingAdmin

    meter = models.ForeignKey(
        "core.WaterMeter",
        on_delete=models.CASCADE,
        verbose_name="Счетчик",
    )
    date = models.PositiveSmallIntegerField(verbose_name="Месяц", choices=MonthChoices)
    reading = models.PositiveSmallIntegerField("Показания")
    cost = models.PositiveIntegerField("Стоимость", default=0)

    def __str__(self):
        return f"{self.meter} {self.get_date_display()}"
