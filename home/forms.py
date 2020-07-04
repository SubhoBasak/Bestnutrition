from django import forms
from django.contrib.auth.models import User
from . import models


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.fields:
            self.fields[field].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.fields:
            self.fields[field].required = True

    class Meta:
        model = models.Address
        fields = ['first_name', 'last_name', 'phone', 'address', 'city', 'state', 'pin_code']