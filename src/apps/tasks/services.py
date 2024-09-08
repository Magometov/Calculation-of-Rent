from django.utils import timezone


def __update_cost_field_in_reading_model(current_month, cost_reading_for_corrent_month):
    current_month.update(cost=cost_reading_for_corrent_month)


def calculate_water_debt(apartment):
    current_month = timezone.now().month
    last_month = current_month - 1
    consumption = 0
    house = apartment.house
    result = "Информации нет"
    for water_meter in apartment.water_meters.all():
        reading_for_cuttent_month = water_meter.reading.filter(date__month=current_month)
        reading_for_last_month = water_meter.reading.filter(date__month=last_month)
        if reading_for_cuttent_month and reading_for_last_month:
            consumption += reading_for_cuttent_month[0].reading - reading_for_last_month[0].reading

    if price_obj := house.prices.first():
        result = price_obj.price_for_water_supply * consumption
        __update_cost_field_in_reading_model(reading_for_cuttent_month, result)
    return result


def calculate_rent_for_area(apartment):
    result = "Информации нет"
    house = apartment.house
    if price_obj := house.prices.first():
        result = price_obj.price_for_area * apartment.square
    return result
