from django import forms
from .models import Product 


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at','updated','is_active','is_bestseller','is_featured')

    def clean_price(self):
        if self.cleaned_data['price'] <=0:
            raise forms.ValidationError('Price musy be greater than zero.')
        return self.cleaned_data['price']
