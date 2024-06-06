import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_lab.settings')
django.setup()
from customer.models import Customer





results= Customer.objects.filter(name__startswith=("EVIL"))



print(f" the count is: {results.count()}")
print(f" the customer name in slot 0 is {results[0].name}")