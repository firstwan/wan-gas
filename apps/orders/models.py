from django.db import models

# Create your models here.
class Order(models.Model):
    transaction_id = models.CharField(max_length=100)
    before_discount_price = models.DecimalField(max_digits=18, decimal_places=4)
    promotion_discount_amount = models.DecimalField(max_digits=18, decimal_places=4)
    net_price = models.DecimalField(max_digits=18, decimal_places=4)
    created_by = models.CharField(max_length=250)
    created_date = models.DateTimeField()
    buyer = models.ForeignKey(to='customers.Customer', on_delete=models.PROTECT, related_name='orders')
    payment_transaction = models.ForeignKey(to='payments.Payment', on_delete=models.PROTECT, related_name='orders')


    class Meta:
        db_table = "order"


class OrderItem(models.Model):
    product = models.ForeignKey(to='products.Product', on_delete=models.PROTECT, related_name='order_items')
    product_name = models.CharField(max_length=250)
    qty = models.IntegerField()
    product_base_price = models.DecimalField(max_digits=18, decimal_places=4)
    discount_amount = models.DecimalField(max_digits=18, decimal_places=4)
    actual_price = models.DecimalField(max_digits=18, decimal_places=4)
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT, related_name='order_items')


    class Meta:
        db_table = "order_item"
