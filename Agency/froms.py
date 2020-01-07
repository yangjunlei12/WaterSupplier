from django import forms

class AgencyForm(forms.Form):
    name    = forms.CharField(max_length=100)
    phone   = forms.CharField(max_length=25)
    wechat  = forms.CharField(max_length=25)
    qq      = forms.CharField(max_length=15)
    email   = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)

class ProxyForm(forms.Form):
    proxyId   = forms.IntegerField()
    num       = forms.IntegerField()
    unit      = forms.CharField(max_length=25)
    productId = forms.IntegerField()
    time      = forms.DateField()
