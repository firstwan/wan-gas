from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer

# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = []


    @action(detail=True)
    def customPath(self, request, *args, **kwargs):
        return Response("custom api path")

    def perform_create(self, serializer):
        serializer.save(updated_by=self.request.user)