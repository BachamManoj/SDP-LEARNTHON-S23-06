# voter_registration/forms.py
from django import forms
from .models import Voter


class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = '__all__'
