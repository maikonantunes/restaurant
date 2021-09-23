"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls


schema_url = "http://127.0.0.1:8000"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Restaurant API', schema_url=schema_url)),
    path('api/', include(([
        path('ingredient/', include('ingredient.urls', namespace='ingredient')),
        path('method_preparation/', include('method_of_preparation.urls', namespace='method_preparation')),
        path('recipes/', include('recipes.urls', namespace='recipes')),
        path('users/', include('users.urls', namespace='users')),
        path('authentication/', include('authentication.urls', namespace='authentication')),
    ], 'api'))),
]
