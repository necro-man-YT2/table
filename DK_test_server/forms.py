from django import forms

class Player(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    address = forms.CharField()