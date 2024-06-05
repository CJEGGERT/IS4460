import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_lab.settings')
django.setup()
from customer.models import Customer

customer1 = Customer()

customer1.name = "XYZ Corp"

customer1.save()
