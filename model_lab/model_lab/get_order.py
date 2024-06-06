import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_lab.settings')
django.setup()
from customer.models import Customer,Order


order = Order.objects.get(id=1)

print(order.customer.name)
