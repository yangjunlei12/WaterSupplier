from django import forms

class ProductForm(forms.Form):
    title      = forms.CharField(max_length=30, label="题目") 
    images     = forms.ImageField(label="图片")
    abstract   = forms.CharField(max_length=100, label="摘要")
    content    = forms.CharField(max_length=200, label="内容")
    cultureId  = forms.IntegerField()
    sales      = forms.IntegerField()
    quantity   = forms.FloatField()
    price      = forms.FloatField()
    discount   = forms.FloatField()  

    def clean(self):
        return self.cleaned_data
