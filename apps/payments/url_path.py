from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter
from . import views

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register('payments', views.PaymentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)