from django.db import models
from django.db import models

# Create your models here.
class Order(models.Model):
    UniqueId = models.UUIDField()
    BeforeDiscountPrice = models.DecimalField(max_digits=18, decimal_places=4)
    PromotionDiscountAmount = models.DecimalField(max_digits=18, decimal_places=4)
    NetPrice = models.DecimalField(max_digits=18, decimal_places=4)
    PaymentTransactionId = models.UUIDField()
    CreatedBy = models.CharField(max_length=250)
    CreatedDate = models.DateTimeField()
    BuyerId = models.UUIDField()


    class Meta:
        db_table = "order"


class OrderItem(models.Model):
    ProductUniqueId = models.UUIDField()
    ProductName = models.CharField(max_length=250)
    Qty = models.IntegerField()
    ProductBasePrice = models.DecimalField(max_digits=18, decimal_places=4)
    DiscountAmount = models.DecimalField(max_digits=18, decimal_places=4)
    ActualPrice = models.DecimalField(max_digits=18, decimal_places=4)


    class Meta:
        db_table = "order_item"
