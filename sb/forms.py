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

class login_form(forms.Form):
    user_name = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'User Name', 'class': 'form-control', 'id': 'inputUsername'}), required=True)
    user_pass = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'id': 'inputPassword'}), required=True)