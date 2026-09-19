from django import forms
from store1.models.Category import Category


class VendorCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']