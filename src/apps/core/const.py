from django.db import models


class CityChoices(models.IntegerChoices):
    msc = 0, "Москва"
    spb = 1, "Санкт-Петербург"
