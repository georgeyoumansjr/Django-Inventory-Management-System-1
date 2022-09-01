from django import forms
from .models import Available_product_table

class AddProductForm(forms.ModelForm):
    product_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Product Name'}))
    product_price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Product Price'}))
    product_quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Quantity'}))

    class Meta():
        model = Available_product_table
        fields = '__all__'


class SearchForm(forms.Form):
    search_product = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Product Name','class':'form-control my-0 py-1'}))
