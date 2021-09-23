from django.contrib import admin
from .models import MethodPreparation


@admin.register(MethodPreparation)
class AuthorAdmin(admin.ModelAdmin):
    pass
