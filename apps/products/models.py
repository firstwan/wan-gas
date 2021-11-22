from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    base_price = models.DecimalField(max_digits=18, decimal_places=4)
    qty_in_stock = models.IntegerField()
    created_by = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=250)
    updated_date = models.DateTimeField(null=True)

    class Meta:
        db_table = "product"

# class ProductHistoryType(models.Model):
#    Name = models.CharField(max_length=100)
#    Description = models.CharField(max_length=250)

class ProductHistory(models.Model):
    class ProductHistoryType(models.IntegerChoices):
        RESTOCK = 1
        SELL = 2
        MANUAL_ADJUST = 3

    history_type_id = models.IntegerField(choices=ProductHistoryType.choices)
    history_type_name = models.CharField(max_length=50)
    qty = models.IntegerField()
    remark = models.CharField(max_length=250)
    created_by = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    action_reference_id = models.CharField(max_length=100)
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)


    class Meta:
        db_table = "product_history"


