from django import forms



class HomeForm(forms.Form):
    age_months = forms.IntegerField(required=False, label = "Age", help_text = "months")
    height_cm = forms.IntegerField(required=False, label = "Height", help_text = "cm")
    weight_kg = forms.IntegerField(required=False, label = "Weight", help_text = "kg")
    amp_0_to_10 = forms.IntegerField(required=False, label = "Amp", help_text = "0-10")
    purpose = forms.ChoiceField(required=False, choices=((0.1,'-'),(0,'0'),(0.1, '+')))