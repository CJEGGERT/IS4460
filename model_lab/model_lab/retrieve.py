import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_lab.settings')
django.setup()
from customer.models import Customer

all_customers= Customer.objects.all()

print(f"customers; {all_customers}")

