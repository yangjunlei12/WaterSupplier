"""WaterSupplier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Company.views as views
from Image.views import upload_image

'''
articleAPI/ + ...
'''
urlpatterns = [
#    path(r'news/(?P<company_id>\d+)/$', views.get_news),
#    path(r'activities/(?P<company_id>\d+)/$', views.get_activities),
    path('activities_count', views.get_activities_count),
    path(r'article/(?P<id>\d+)/$', views.get_article),
    path('test', views.test_func),
    path('companies', views.render_table),
    path('addcompany', views.create_com),
    # path('addarticle', views.add_article),

    path('getCompanies', views.all_cqmpanies),
    path('getList', views.get_list),
    path('getCategories', views.get_categories),

    path('uploadCover', upload_image),
    path('uploadImg', upload_image),

    path('commitArticle', views.commitArticle),
]
