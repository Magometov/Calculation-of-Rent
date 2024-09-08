from django.core.exceptions import ValidationError
from django.db import models

from src.apps.core.models.admins.WaterMeterReadingModelAdmin import (
    WaterMeterReadingAdmin,
)


class WaterMeterReading(models.Model):
    class Meta:
        verbose_name = "Показания счетчика"
        verbose_name_plural = "Показании счетчика"
        default_related_name = "reading"

    ModelAdmin = WaterMeterReadingAdmin

    meter = models.ForeignKey(
        "core.WaterMeter",
        on_delete=models.CASCADE,
        verbose_name="Счетчик",
    )
    date = models.DateField(verbose_name="Дата")
    reading = models.PositiveSmallIntegerField("Показания")
    cost = models.PositiveIntegerField("Стоимость", default=0)

    def save(self, *args, **kwargs):
        if WaterMeterReading.objects.filter(meter=self.meter, date=self.date).exclude(id=self.id).exists():
            raise ValidationError("На этот месяц показания счетчика уже записаны.")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.meter} | Показания на {self.date.month}.{self.date.year}"
