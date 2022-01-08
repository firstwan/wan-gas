from django.db import models

# Create your models here.
class PaymentMethod(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = "payment_method"
    
class Payment(models.Model):
    class PaymentType(models.IntegerChoices):
        ORDER = 1

        def __str__(self):
            return str(self.label)

    transaction_id = models.CharField(max_length=100)
    payment_type_id = models.IntegerField(choices=PaymentType.choices)
    payment_type_name = models.CharField(max_length=50, choices=PaymentType.choices, default=PaymentType.ORDER)
    amount = models.DecimalField(max_digits=18, decimal_places=4)
    created_by = models.CharField(max_length=250)
    created_date = models.DateTimeField()
    action_reference_id = models.CharField(max_length=250)
    payer = models.ForeignKey(to='customers.Customer', on_delete=models.PROTECT, related_name='payments')
    payment_method = models.ForeignKey(to=PaymentMethod, on_delete=models.PROTECT, related_name='payments')


    class Meta:
        db_table = "payment"
