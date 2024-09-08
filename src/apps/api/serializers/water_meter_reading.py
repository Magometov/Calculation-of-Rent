from rest_framework import serializers

from src.apps.core.models import WaterMeterReading


class WaterMeterReadingSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%m.%Y")

    class Meta:
        model = WaterMeterReading
        fields = [
            "date",
            "reading",
            "cost",
        ]
