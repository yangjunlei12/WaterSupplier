from django import forms
from Products.models import ProductModel, ProductType

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        exclude = ['like', 'share', 'sales', 'create', 'cultureId', 'quantity']

class TypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        exclude = []


# class ProductForm(forms.Form):
#     title      = forms.CharField(max_length=30, label="题目") 
#     images     = forms.ImageField(label="图片")
#     abstract   = forms.CharField(max_length=100, label="摘要")
#     content    = forms.CharField(max_length=200, label="内容")
#     cultureId  = forms.IntegerField()
#     sales      = forms.IntegerField()
#     quantity   = forms.FloatField()
#     price      = forms.FloatField()
#     discount   = forms.FloatField()  

#     def clean(self):
#         return self.cleaned_data
