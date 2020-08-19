from django import forms



class HomeForm(forms.Form):
    age_months = forms.IntegerField(required=False)
    height_cm = forms.IntegerField(required=False)
    weight_kg = forms.IntegerField(required=False)
    amp_0_to_10 = forms.IntegerField(required=False)
    purpose = forms.IntegerField(required=False)