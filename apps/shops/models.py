from platform import release
from pyexpat import model
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
    products = models.ManyToManyField('products.Product', through='ProductPrice', related_name='shops')
    created_by = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=250)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = "shop"

# Many-to-Many table
class ProductPrice(models.Model):
    shop = models.ForeignKey(to=Shop, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(to='products.Product', related_name='product_price', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=4)
