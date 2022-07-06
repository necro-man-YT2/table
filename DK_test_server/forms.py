from django import forms

class Player(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    address = forms.CharField()


class DateForms(forms.Form):
    pull1 = forms.IntegerField()
    pull2 = forms.IntegerField()
    push1 = forms.IntegerField()
    push2 = forms.IntegerField()
    sit1 = forms.IntegerField()
    sit2 = forms.IntegerField()
    jumping1 = forms.IntegerField()
    jumping2 = forms.IntegerField()
    entrance1 = forms.IntegerField()
    entrance2 = forms.IntegerField()
    press1 = forms.IntegerField()
    press2 = forms.IntegerField()
    weight1 = forms.IntegerField()
    weight2 = forms.IntegerField()
    weightcategory1 = forms.IntegerField()
    weightcategory2 = forms.IntegerField()
    bars1 = forms.IntegerField()
    bars2 = forms.IntegerField()
    stadium1 = forms.IntegerField()
    stadium1 = forms.IntegerField()
