import logging

from celery import shared_task

from src.apps.core.models import House
from src.apps.tasks.services import calculate_rent_for_area, calculate_water_debt
from src.config.celery import app

logger = logging.getLogger("django")

"""
Результат работы таски можно было собирать в exel таблицу и отправлять в тг или на почту, например.
"""


@shared_task(queue="periodic")
def utilities_data(house_id):
    result = {}
    house = House.objects.get(id=house_id)
    apartment_list = house.apartments.all()
    result["Всего квартир в доме"] = len(apartment_list)

    for apartment in apartment_list:
        water_debt = calculate_water_debt(apartment)
        rent_for_area = calculate_rent_for_area(apartment)

        result[apartment.__str__()] = {
            "Команалка по воде": water_debt,
            "Комуналка по площади кв": rent_for_area,
        }

    return result


@app.task(name="test_celery_task")
def test_celery_task() -> str:
    return "Gooooooooood"
