from .models import Address
from django import forms

#create forms and modelforms here
class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = "__all__"
