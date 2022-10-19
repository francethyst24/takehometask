from django import forms

class CountryForm(forms.Form):
    query_country = forms.CharField(label='Queried country', max_length=100)