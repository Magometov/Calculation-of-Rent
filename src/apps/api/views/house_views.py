from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from src.apps.api.serializers.house import HouseSerializer
from src.apps.core.models import House


@api_view(["POST"])
def get_house_data(request):
    house_id = request.data.get("house_id")

    if house_id is None:
        return Response({"detail": "id дома не передан"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        house = get_object_or_404(House, id=house_id)
    except Http404:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = HouseSerializer(house)
    return Response(serializer.data)
