from django import forms

from sb.models import customer

class customer_form(forms.ModelForm):
    class Meta:
        model = customer
        fields = [
            'first_name',
            'last_name',
            'home_phone',
            'cell_phone',
            'email',
            'full_address',
            'alt_address',
            'city',
            'state',
            'zip_code',
        ]