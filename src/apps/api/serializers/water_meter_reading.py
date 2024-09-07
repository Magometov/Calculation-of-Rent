from rest_framework import serializers

from src.apps.core.models import WaterMeterReading


class WaterMeterReadingSerializer(serializers.ModelSerializer):
    date = serializers.CharField(source="get_date_display")

    class Meta:
        model = WaterMeterReading
        fields = [
            "date",
            "reading",
            "cost",
        ]
