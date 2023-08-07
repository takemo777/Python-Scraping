from django import forms

class Radio(forms.Form):
    num = forms.IntegerField(min_value=0)
    
    