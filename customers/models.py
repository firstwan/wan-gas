from django.db import models

# Create your models here.
class Customer(models.Model):
    UniqueId = models.UUIDField()
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)

    class Meta:
        db_table = "customer"

class Contact(models.Model):
    class ContactType(models.IntegerChoices):
        MOBILE_NUMBER = 1
        EMAIL = 2
    
    ContactTypeId = models.IntegerField(choices=ContactType.choices)
    ContactTypeName = models.CharField(max_length=50)
    ContactValue = models.CharField(max_length=250)
    CustomerId = models.ForeignKey(to=Customer, on_delete=models.PROTECT)


    class Meta:
        db_table = "customer_contact"