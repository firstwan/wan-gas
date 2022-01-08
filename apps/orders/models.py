from django.db import models

# Create your models here.
class Order(models.Model):
    class OrderStatus(models.IntegerChoices):
        CREATED = 1,
        PENDING_PAYMENT = 2,
        COMPLETE = 3

        def __str__(self):
            return str(self.label)

    transaction_id = models.CharField(max_length=100)
    order_status_id = models.IntegerField(choices=OrderStatus.choices, default=OrderStatus.CREATED)
    order_status_name = models.CharField(max_length=50, choices=OrderStatus.choices, default=OrderStatus.CREATED)
    before_discount_price = models.DecimalField(max_digits=18, decimal_places=4)
    promotion_discount_amount = models.DecimalField(max_digits=18, decimal_places=4)
    net_price = models.DecimalField(max_digits=18, decimal_places=4)
    created_by = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(to='shops.Shop', on_delete=models.PROTECT, related_name='orders')
    payment_transaction = models.ForeignKey(to='payments.Payment', on_delete=models.PROTECT, related_name='orders', null=True)


    class Meta:
        db_table = "order"


class OrderItem(models.Model):
    product = models.ForeignKey(to='products.Product', on_delete=models.PROTECT, related_name='order_items')
    product_name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    product_base_price = models.DecimalField(max_digits=18, decimal_places=4)
    discount_amount = models.DecimalField(max_digits=18, decimal_places=4)
    actual_price = models.DecimalField(max_digits=18, decimal_places=4)
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT, related_name='order_items')


    class Meta:
        db_table = "order_item"
