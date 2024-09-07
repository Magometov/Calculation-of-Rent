from rest_framework import serializers

from src.apps.api.serializers.apartment import ApartmentSerializer
from src.apps.core.models import House


class HouseSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source="get_city_display")
    apartments = ApartmentSerializer(many=True)

    class Meta:
        model = House
        fields = [
            "city",
            "district",
            "address",
            "apartments",
        ]
