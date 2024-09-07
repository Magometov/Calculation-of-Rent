from django.db import models


class CityChoices(models.IntegerChoices):
    msc = 0, "Москва"
    spb = 1, "Санкт-Петербург"


class MonthChoices(models.IntegerChoices):
    january = 0, "Январь"
    february = 1, "Февраль"
    march = 2, "Март"
    april = 3, "Апрель"
    may = 4, "Май"
    june = 5, "Июнь"
    july = 6, "Июль"
    august = 7, "Август"
    september = 8, "Сентябрь"
    october = 9, "Октябрь"
    november = 10, "Ноябрь"
    december = 11, "Декабрь"
    __empty__ = "Не выбрано"
