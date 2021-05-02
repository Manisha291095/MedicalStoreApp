from django import forms
from medical.models import Medicines

class MedicinesForm(forms.ModelForm):
    class Meta:
        model = Medicines
        fields = "__all__"