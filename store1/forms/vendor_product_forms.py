from django import forms
from store1.models.Product import Products

class VendorProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=['name', 'price', 'category', 'description', 'image']