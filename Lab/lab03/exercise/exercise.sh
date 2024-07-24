#! /usr/bin/bash

python manage.py shell

>>> from shop.models import Order, Product, ProductCategory

# Query Data from Database

# exercise 01

>>> for o in Order.objects.filter(order_date__month = 5)[:10]:
>>> 	print(f"ORDER ID:{o.id}, DATE: {o.order_date}, PRICE: {o.payment.price}")

# exercise 02

>>> for p in Product.objects.filter(description__endswith = "features."):
>>>	print(f"PRODUCT ID: {p.id}, DESCRIPTION: {p.description}")

# exercise 03

>>> for p in Product.objects.filter(price__gte = 5000):
>>> 	print(f"PRODUCT ID: {p.id}, NAME: {p.name}, PRICE: {p.price}")

# exercise 04

>>> for p in Product.objects.filter(price__lt = 200, price__gt = 100):
>>>	print(f"PRODUCT ID: {p.id}, NAME: {p.name}, PRICE: {p.price}")

# INSERT UPDATE DELETE

# exercise 01

>>> p1 = Product(name = "Philosopher's Stone (1997)", description = "By J. K. Rowling", remaining_amount = 20, price = 790)
>>> p1.save()
>>> p1.categories.add(7)
>>>
>>> p2 = Product(name = "Me Before You", description = "A romance novel written by Jojo", remaining_amount = 40, price = 390)
>>> p2.save()
>>> p2.categories.add(7)
>>>
>>> p3 = Product(name = "Notebook HP Pavilion Silver", description = "Display Screen. 16.0", remaining_amount = 10, price = 20000)
>>> p3.save()
>>> p3.categories.add(1, 2)

# exercise 02

>>> p1.name = "Half-Blood Prince (2005)"
>>> p1.save()

# exercise 03

>>> book = ProductCategory.objects.get(pk = 7)
>>> book.name = "Books"

# exercise 04

>>> Product.objects.filter(categories = 7).delete()

