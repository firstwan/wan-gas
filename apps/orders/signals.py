from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Order
from ..payments.models import Payment

@receiver(post_save,  sender='payments.Payment')
def payment_created(sender, instance, created, **kwargs): 
    if created and instance.payment_type_id == int(Payment.PaymentType.ORDER):
        order = Order.objects.get(transaction_id = instance.action_reference_id)
        order.payment_transaction_id = instance.id

        if instance.payment_status_id == int(Payment.PaymentStatus.COMPLETE):
            order.order_status_id = Order.OrderStatus.COMPLETE
            order.order_status_name = Order.OrderStatus.COMPLETE

        order.save()