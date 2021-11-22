from rest_framework import viewsets, mixins
from .models import Order
from .serializers import OrderSerializer

# Create your views here.
class OrderViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []
    http_method_names = [ method 
                          for method in viewsets.ModelViewSet.http_method_names 
                          if method not in ['delete']
    ]
