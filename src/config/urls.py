from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("src.apps.api.urls.common_urls", namespace="api")),
]
