from django import forms

class CompanyForm(forms.Form):
    name          = forms.CharField(max_length=50)
    logo          = forms.CharField( max_length=50)
    member_status = forms.IntegerField()
    phone         = forms.CharField(max_length=25)
    wechat        = forms.CharField(max_length=25)
    qq            = forms.CharField(max_length=15)
    email         = forms.CharField(max_length=50)
    address       = forms.CharField(max_length=100)
    
class ArticleForm(forms.Form):
    company_id    = forms.IntegerField()
    ### True是动态 False 是活动
    type          = forms.BooleanField()
    content       = forms.CharField(max_length=500)
    title         = forms.CharField(max_length=200)
    abstract      = forms.CharField(max_length=250)
    images        = forms.CharField(max_length=500)
    status        = forms.BooleanField() 
    create_time   = forms.DateField()
    visits        = forms.IntegerField()
    likes         = forms.IntegerField()
    shares        = forms.IntegerField()
    member_status = forms.IntegerField()
