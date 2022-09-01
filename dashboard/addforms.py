from django import forms
from .models import Available_product_table
class AddProductForm(forms.ModelForm):
    product_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Product Name'}))
    product_price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Product Price'}))
    product_quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Quantity'}))

    class Meta():
        model = Available_product_table
        fields = '__all__'