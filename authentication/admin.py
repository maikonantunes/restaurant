from django.contrib import admin
from .models import User


@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    pass
