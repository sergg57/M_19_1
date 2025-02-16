"""
URL configuration for gamesShop project.

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
from django.urls import path
from django.views.generic import TemplateView
from task4.views import platform_view, games_view, cart_view
from task5.views import sign_up_by_django, sign_up_by_html
from task1.views import news

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('platform/', platform_view),
    path('platform/games/', games_view),
    path('platform/cart/', cart_view),
    path('platform/news/', news),
    path('task5/', sign_up_by_html),
    path('task5/form/', sign_up_by_django),
]

