from django.db import models

# Create your models here.
class Shop(models.Model):
    Name = models.CharField(max_length=250)
    Address1 = models.CharField(max_length=250)
    Address2 = models.CharField(max_length=250)
    AddressPostcode = models.IntegerField()
    AddressCity= models.CharField(max_length=100)
    AddressState = models.CharField(max_length=100)
    OwnerId = models.UUIDField()
    Nickname = models.CharField(max_length=100)


    class Meta:
        db_table = "shop"