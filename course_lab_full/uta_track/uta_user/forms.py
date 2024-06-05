from django.forms import ModelForm
from .models import UtaUser


class UserForm(ModelForm):
    class Meta:
        model = UtaUser
        fields = ['my_routes',]