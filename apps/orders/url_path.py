from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter
from .views import OrderViewset

router = SimpleRouter()
router.register('orders', OrderViewset)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)