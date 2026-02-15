from django import forms

class inputFrom(forms.Form):
    textField = forms.CharField(label="Enter a Text", max_length=50)