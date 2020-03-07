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
from django.urls import path, re_path
import Products.views as views


'''
 productAPI/ + ...
'''
urlpatterns = [
    re_path(r'product/', views.get_product_info),
    re_path(r'add/(?P<company_id>\d+)/$', views.add_product),
    re_path(r'show/(?P<company_id>\d+)/$', views.show_com_pro),

    path('getCompanys', views.all_cqmpanies),
    path('getList/', views.get_product_list),
    re_path(r'getCategory/', views.get_company_product),

    path('uploadCover', views.uploadCover),
    path('uploadDetailImg', views.upload_detail),
    path('commitProduct', views.commitProduct),
    path('addCategory', views.add_category),
]
