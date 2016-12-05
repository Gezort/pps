from django import forms

class OrderIdForm(forms.Form):
    id = forms.IntegerField(widget=forms.TextInput(), min_value=0)