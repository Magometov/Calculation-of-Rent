from rest_framework import serializers

from src.apps.api.serializers.water_meter_reading import WaterMeterReadingSerializer
from src.apps.core.models import WaterMeter


class WaterMeterSerializer(serializers.ModelSerializer):
    reading = WaterMeterReadingSerializer(many=True)

    class Meta:
        model = WaterMeter
        fields = [
            "serial_number",
            "reading",
        ]
