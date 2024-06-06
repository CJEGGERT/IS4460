import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_lab.settings')
django.setup()
from customer.models import Customer

a_customer = Customer.objects.get(id=3)
a_customer.name = "Matts AI Company"
a_customer.save()

