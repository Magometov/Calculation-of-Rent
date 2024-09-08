import logging

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from src.apps.core.models import House
from src.apps.tasks.tasks.public_utilities.calculating_utilities import utilities_data

logger = logging.getLogger("django")


@api_view(["POST"])
def call_task_for_calculating_utilities(request):
    house_id = request.data.get("house_id")
    logger.warning("*" * 55)
    logger.warning("Я блять во вьюзе сука")
    if house_id is None:
        return Response({"detail": "id дома не передан"}, status=status.HTTP_400_BAD_REQUEST)

    if House.objects.filter(id=house_id).exists():
        utilities_data.delay(house_id)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
