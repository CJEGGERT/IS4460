import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_lab.settings')
django.setup()
from customer.models import Customer

best_org_cust = Customer.objects.get(name='Best_Org_Ever')

best_org_cust.delete()