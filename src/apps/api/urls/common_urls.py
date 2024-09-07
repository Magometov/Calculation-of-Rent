from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("house/", include("src.apps.api.urls.house_urls")),
]
