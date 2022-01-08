from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import ProductHistory

@receiver(post_save, sender='orders.OrderItem')
def finish_order(sender, **kwargs): 
    obj=kwargs['instance']
    product = obj.product

    product.qty_in_stock -= obj.quantity
    product.save()

    # Insert product history record
    ProductHistory.objects.create(
        history_type_id = ProductHistory.ProductHistoryType.SELL,
        history_type_name = ProductHistory.ProductHistoryType.SELL,
        qty = obj.quantity,
        remark = f'Sell with order {obj.order.transaction_id}',
        created_by = 'order Item - finish_order signal',
        action_reference_id = obj.order.transaction_id,
        product = product
    )

