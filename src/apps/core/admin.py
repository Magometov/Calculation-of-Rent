from django.contrib import admin
from django.contrib.auth.models import Group, User

from src.apps.core.models import Models

admin.site.unregister(Group)
admin.site.unregister(User)

for model in Models:
    admin.site.register(model.value, model.value.ModelAdmin)

admin.site.site_header = "Администрирование ЖКХ"
admin.site.index_title = "Панель администрирования"
