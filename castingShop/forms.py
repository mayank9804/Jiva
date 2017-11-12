from django import forms
from .models import *

PRODUCT_QUANTITY_CHOICES_IN_TONS = [(i,str(i)) for i in range(1,21)]

class ProductForm(forms.ModelForm):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES_IN_TONS,coerce=int)
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
    class Meta:
        exclude = ("total_cost","company_profit")
        # fields = ('first_name','last_name','email','address','postal_code','city')
        model = Orders



class CustomizeForm(forms.ModelForm):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES_IN_TONS,coerce=int)
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
    class Meta:
        exclude = ("total_cost","company_profit")
        # fields = ('first_name','last_name','email','address','postal_code','city')
        model = CustomizeOrders
