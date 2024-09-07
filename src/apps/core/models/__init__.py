from enum import Enum

from src.apps.core.models.ApartmentModel import Apartment
from src.apps.core.models.HouseModel import House
from src.apps.core.models.PriceModel import Price
from src.apps.core.models.WaterMeterModel import WaterMeter
from src.apps.core.models.WaterMeterReadingModel import WaterMeterReading


class Models(Enum):
    house = House
    apartment = Apartment
    water_meter = WaterMeter
    water_meter_reading = WaterMeterReading
    price = Price
