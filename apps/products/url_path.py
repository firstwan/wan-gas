from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .import views

router = SimpleRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]