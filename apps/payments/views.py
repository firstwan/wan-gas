import uuid
from datetime import datetime
from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Payment
from .serializers import PaymentSerializer


# Filter
class PaymentFitler(filters.FilterSet):
    created_start_date = filters.DateTimeFilter(field_name="created_date", lookup_expr='gte')
    created_end_date = filters.DateTimeFilter(field_name="created_date", lookup_expr='lte')

    class Meta:
        model = Payment
        fields = ['transaction_id', 'payer_id']

# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_class = PaymentFitler

    def get_queryset(self):

        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        same_referent_id_payment = Payment.objects.filter(action_reference_id = self.request.data['action_reference_id'])
        if same_referent_id_payment.count() > 0:
            return Response({'message': f'Duplicate {self.request.data["action_reference_id"]} action reference id.'}, status=status.HTTP_409_CONFLICT)
        else:
            return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(transaction_id=self.generate_transaction_id(),
                        created_by=self.request.user,
                        payment_status_id = Payment.PaymentStatus.COMPLETE if self.request.data['payment_method_id'] == '1' else Payment.PaymentStatus.PENDING)


    # Own defined method
    def generate_transaction_id(self):
        prefix = 'PAY'
        current_date = datetime.today().strftime('%Y%m%d%H%M%S')
        unique_id = str(uuid.uuid4())[:8]

        return prefix + current_date + unique_id.upper()