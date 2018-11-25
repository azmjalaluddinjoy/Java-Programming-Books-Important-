from django import forms
from .models import Product
from .models import Newusers, Nuser

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = Nuser
        fields = [
            'name',
            'phone',
            'address',
            'occupation',
            'email',
            'password',
            'image'
        ]
#
# class customerFOrm(forms.ModelForm)
#     class Meta:
#         model = customer
#         fields = [
#
#         ]