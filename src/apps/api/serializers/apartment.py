from rest_framework import serializers

from src.apps.api.serializers.water_meter import WaterMeterSerializer
from src.apps.core.models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    water_meters = WaterMeterSerializer(many=True)

    class Meta:
        model = Apartment
        fields = [
            "number",
            "square",
            "water_meters",
        ]
