"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import HttpResponse
from django.shortcuts import render

# Пример простого представления для главной страницы
def home(request):
    return render(request, 'layoute.html')

urlpatterns = [
    path('admin/', admin.site.urls),       # Админка
    path('', home, name='home'),           # Маршрут для главной страницы
    path('news/', include('news.urls')),   # Маршрут для приложения news
]
from django.urls import path

