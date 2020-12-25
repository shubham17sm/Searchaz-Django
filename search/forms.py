from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=225, label='Query')
    query_num = forms.IntegerField(label='Number of query', required=True)
    