from django import forms
from mdeditor.fields import MDTextFormField
from Company.models import CompanyModel, ArticleModel

class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyModel
        exclude = ['id', ]

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        exclude = ['visits', 'likes', 'shares', 'create_time','status', 'member_status']
        labels  = {
            'type': '类型',
            'title': '标题',
            'images': '图片',
            'abstract': '摘要',
            # 'status': '状态',
            # 'member_status': '会员状态',
            'content': '内容',
        }
        # widgets = {
        #     'images': forms.ImageField,
        # }


# class CompanyForm(forms.Form):
#     name          = forms.CharField(max_length=50)
#     logo          = forms.CharField( max_length=50)
#     member_status = forms.IntegerField()
#     phone         = forms.CharField(max_length=25)
#     wechat        = forms.CharField(max_length=25)
#     qq            = forms.CharField(max_length=15)
#     email         = forms.CharField(max_length=50)
#     address       = forms.CharField(max_length=100)
    
# class ArticleForm(forms.Form):
#     company_id    = forms.IntegerField()
#     ### True是动态 False 是活动
#     type          = forms.BooleanField()
#     # content       = forms.CharField(max_length=500)
#     title         = forms.CharField(max_length=200)
#     abstract      = forms.CharField(max_length=250)
#     images        = forms.CharField(max_length=500)
#     status        = forms.BooleanField() 
#     create_time   = forms.DateField()
#     visits        = forms.IntegerField()
#     likes         = forms.IntegerField()
#     shares        = forms.IntegerField()
#     member_status = forms.IntegerField()
#     content       = MDTextFormField()
