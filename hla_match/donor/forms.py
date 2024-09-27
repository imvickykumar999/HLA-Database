from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['first_name', 'last_name', 'email', 'hla_a', 'hla_b', 'hla_c', 'hla_drb1']
