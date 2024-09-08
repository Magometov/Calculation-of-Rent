from django.urls import path

from src.apps.api.views.public_utilities_views import (
    call_task_for_calculating_utilities,
)

urlpatterns = [
    path("", call_task_for_calculating_utilities),
]
