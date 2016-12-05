from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'groups')

class GroupForm(forms.Form):
    GROUPS = {
            0 : 'user',
            1 : 'courier'
    }
    group = forms.ChoiceField(choices=GROUPS.items(), initial=0, widget=forms.Select())