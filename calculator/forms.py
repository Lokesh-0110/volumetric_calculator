from django import forms  # ✅ Correct
# Do NOT import from .forms here

class ParcelForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    weight = forms.FloatField(min_value=0)
    length = forms.FloatField(min_value=0)
    width = forms.FloatField(min_value=0)
    height = forms.FloatField(min_value=0)
    unit = forms.ChoiceField(choices=[('kg/cm', 'kg/cm'), ('lb/in', 'lb/in')])
