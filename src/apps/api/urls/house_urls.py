from django.urls import path

from src.apps.api.views.house_views import get_house_data

urlpatterns = [
    path("", get_house_data),
]
