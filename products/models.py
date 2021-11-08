from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=250)
    BasePrice = models.DecimalField(max_digits=18, decimal_places=4)
    QtyInStock = models.IntegerField()
    CreatedBy = models.CharField(max_length=250)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedBy = models.CharField(max_length=250)
    UpdatedDate = models.DateTimeField(null=True)

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

    HistoryTypeId = models.IntegerField(choices=ProductHistoryType.choices)
    HistoryTypeName = models.CharField(max_length=50)
    Qty = models.IntegerField()
    Remark = models.CharField(max_length=250)
    CreatedBy = models.CharField(max_length=250)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    ActionReferenceId = models.CharField(max_length=100)


    class Meta:
        db_table = "product_history"


