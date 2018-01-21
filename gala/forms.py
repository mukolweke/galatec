from django import forms
from django.contrib.auth.models import User

from shop.models import Category, Products


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'slug']


# class ProductForm(forms.ModelForm):
#
#     class Meta:
#         model = Products
#         fields = ['category', 'name', 'slug', 'image', 'description', 'price', 'stock']

#
# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
