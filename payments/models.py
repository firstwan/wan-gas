from django.db import models
from django.db import models

# Create your models here.
class PaymentMethod(models.Model):
    Name = models.CharField(max_length=150)

    class Meta:
        db_table = "payment_method"
    
class Payments(models.Model):
    UniqueId = models.UUIDField()
    Amount = models.DecimalField(max_digits=18, decimal_places=4)
    CreatedBy = models.CharField(max_length=250)
    CreatedDate = models.DateTimeField()
    ActionReferenceId = models.UUIDField()
    PayerId = models.UUIDField()
    PaymentMethodId = models.ForeignKey(to=PaymentMethod, on_delete=models.PROTECT)


    class Meta:
        db_table = "payment"
