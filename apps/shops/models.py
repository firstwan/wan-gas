from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=250)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, null=True)
    address_postcode = models.IntegerField()
    address_city= models.CharField(max_length=100)
    address_state = models.CharField(max_length=100)
    owner = models.ForeignKey(to='customers.Customer', on_delete=models.PROTECT, related_name='shops')
    nickname = models.CharField(max_length=100, null=True)


    class Meta:
        db_table = "shop"