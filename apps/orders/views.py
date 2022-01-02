from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Order
from .serializer import OrderSerializer
import uuid
from datetime import datetime

# Create your views here.
class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = [ method 
                          for method in viewsets.ModelViewSet.http_method_names 
                          if method not in ['delete']
                        ]

    def perform_create(self, serializer):
        serializer.save(
            transaction_id = self.generate_transaction_id(), 
            created_by = self.request.user)             


    # Own defined method
    def generate_transaction_id(self):
        prefix = 'ORD'
        current_date = datetime.today().strftime('%Y%m%d%H%M%S')
        unique_id = str(uuid.uuid4())[:8]

        return prefix + current_date + unique_id.upper()
