from django import forms

class OrderIdForm(forms.Form):
    id = forms.IntegerField(min_value=0)

class ConfigureOrderForm(forms.Form):
    start_location = forms.IntegerField(min_value=0, required=True)
    finish_location = forms.IntegerField(min_value=0, required=True)
    criteria = forms.ChoiceField(choices=((0, 'time'), (1, 'cost')))