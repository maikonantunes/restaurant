from django.contrib import admin
from .models import Recipes


@admin.register(Recipes)
class AuthorAdmin(admin.ModelAdmin):
    pass
