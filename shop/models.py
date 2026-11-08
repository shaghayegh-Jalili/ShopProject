from django.contrib.auth.models import User
from django.db import models

class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False, editable=False)
    updated = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()
        #this method makes the deleted ones be kept in database with a deleted true flag

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    quantity = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) # the difference between auto now and auto now add is that auto now add is unchangeable
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title

class Cart(BaseModel):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(BaseModel):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(null=True)
    created = models.DateTimeField(auto_now_add=True)

class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default=None, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

class PaymentLog(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.PositiveIntegerField()
    order_id = models.PositiveIntegerField()
    status = models.CharField(max_length=100)
    error_code = models.CharField(max_length=200)