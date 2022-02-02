from django.db import models
import uuid


# Create your models here.
class Customer(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    created_by = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=250)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer"

class Contact(models.Model):
    class ContactType(models.IntegerChoices):
        MOBILE_NUMBER = 1
        EMAIL = 2
    
    contact_type_id = models.IntegerField(choices=ContactType.choices)
    contact_type_name = models.CharField(max_length=50)
    contact_value = models.CharField(max_length=250)
    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT)


    class Meta:
        db_table = "customer_contact"