from django import forms

class AddProductForm(forms.Form):
    product_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Product Name'}))
    product_price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Product Price'}))
    product_quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Quantity'}))
