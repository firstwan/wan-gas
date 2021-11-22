"""WanGasPos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.orders.url_path import router as orders_router
from apps.payments.url_path import router as payments_router

router = DefaultRouter()
router.registry.extend(orders_router.registry)
router.registry.extend(payments_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/products/', include('apps.products.url_path')),
    path('api/v1/customers/', include('apps.customers.url_path')),
    path('api/v1/shops/', include('apps.shops.url_path'))
]
