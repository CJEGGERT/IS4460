import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_lab.settings')
django.setup()
from customer.models import Customer,Order


one_customer= Customer.objects.get(id=2)

new_order = Order()
new_order.price = 23.99
new_order.customer = one_customer

new_order.save()








