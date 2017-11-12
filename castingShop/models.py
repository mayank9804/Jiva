from django.db import models
from django.urls import reverse
# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    image = models.ImageField(upload_to='products/',blank=True)
    description = models.TextField(blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('castingShop:product',args=[self.slug])

# class Orders(models.Model):
#     product = models.ForeignKey(Products,related_name='products')
#     quantity = models.PositiveIntegerField()
#     ownerProfit = models.PositiveIntegerField()
#     estimatedCost = models.PositiveIntegerField()
#
#     class Meta:
#         ordering = ('quantity',)
#         verbose_name = 'Order'
#         verbose_name_plural = 'Orders'
#
#     def __str__(self):
#         return '{}'.format(self.id)
#
#     def get_cost(self):
#         return 28000 * (self.quantity + 0.01)

    #
    # class Meta:
    #     ordering = ('-created',)
    #
    # def __str__(self):
    #     return 'Order {}'.format(self.id)

class Orders(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=300)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    company_profit = models.PositiveIntegerField(blank=False,default=0)
    total_cost = models.PositiveIntegerField(blank=False,default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

class CustomizeOrders(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    company_profit = models.PositiveIntegerField(blank=False,default=0)
    total_cost = models.PositiveIntegerField(blank=False,default=0)
    shape = models.CharField(max_length =250,blank=False)
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)
