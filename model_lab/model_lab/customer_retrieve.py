import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_lab.settings')
django.setup()
from customer.models import Customer

oranges = Customer.objects.get(id=2)

print(f"the customer name is: {oranges.name}")