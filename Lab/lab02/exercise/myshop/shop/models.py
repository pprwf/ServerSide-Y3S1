from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 150)
    address = models.JSONField()

class Cart(models.Model):
    customer_id = models.ForeignKey("shop.Customer", on_delete = models.CASCADE)
    create_date = models.DateTimeField(auto_now_add = True)
    expired_in = models.IntegerField(default = 60)

class CartItem(models.Model):
    cart_id = models.ForeignKey("shop.Cart", on_delete = models.CASCADE)
    product_id = models.ForeignKey("shop.Product", on_delete = models.CASCADE)
    amount = models.IntegerField(default = 1)

class Order(models.Model):
    customer_id = models.ForeignKey("shop.Customer", on_delete = models.CASCADE)
    order_date = models.DateField(auto_now_add = True)
    remark = models.TextField(null = True)

class OrderItem(models.Model):
    order_id = models.ForeignKey("shop.Order", on_delete = models.CASCADE)
    product_id = models.ForeignKey("shop.Product", on_delete = models.CASCADE)
    amount = models.IntegerField(default = 1)

class ProductCategory(models.Model):
    name = models.CharField(max_length = 150)

class Product(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField(null = True)
    remaining_amount = models.IntegerField(default = 0)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    product_categories = models.ManyToManyField("shop.ProductCategory")

class Payment(models.Model):
    order_id = models.ForeignKey("shop.Order", on_delete = models.CASCADE)
    payment_date = models.DateField(auto_now_add = True)
    remark = models.TextField(null = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    discount = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)

class PaymentItem(models.Model):
    payment_id = models.ForeignKey("shop.Payment", on_delete = models.CASCADE)
    order_item_id = models.IntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    discount = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)

class PaymentMethod(models.Model):
    payment_id = models.ForeignKey("shop.Payment", on_delete = models.CASCADE)
    METHOD_CHOICES = {1:"QR", 2:"CREDIT"}
    method = models.IntegerField(choices = METHOD_CHOICES)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
