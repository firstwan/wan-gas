from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api_views import customer_view

urlpatterns = [
    path('', customer_view.CustomerList.as_view(), name='customer-list'),
    path('<int:pk>/', customer_view.CustomerDetail.as_view(), name='customer-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)