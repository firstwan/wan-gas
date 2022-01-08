from django.db import models

# Create your models here.
class PaymentMethod(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = "payment_method"
    
class Payment(models.Model):
    class PaymentType(models.IntegerChoices):
        ORDER = 1

    class PaymentStatus(models.IntegerChoices):
        PENDING = 1
        PROCESSING = 2
        COMPLETE = 3

    transaction_id = models.CharField(max_length=100)
    payment_type_id = models.IntegerField(choices=PaymentType.choices)
    payment_type_name = models.CharField(max_length=50, default=PaymentType.ORDER.label)
    payment_status_id = models.IntegerField(choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    payment_status_name = models.CharField(max_length=20, default=PaymentStatus.PENDING.label)
    amount = models.DecimalField(max_digits=18, decimal_places=4)
    created_by = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=250, null=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    action_reference_id = models.CharField(max_length=250)
    payer = models.ForeignKey(to='customers.Customer', on_delete=models.PROTECT, related_name='payments')
    payment_method = models.ForeignKey(to=PaymentMethod, on_delete=models.PROTECT, related_name='payments')


    class Meta:
        db_table = "payment"
