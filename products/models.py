from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)


class Products(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=6, max_digits=6)
    quantity = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
