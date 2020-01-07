from django.shortcuts import render, render_to_response, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from Products.models import ProductModel
from Products.ProductJsonFactory import ProductJsonFactory as JsonFactory
from Products.forms import ProductForm
from django.views.decorators.csrf import csrf_protect
from utils.ListFactory import make_list
from utils.FormModelSaver import ObjCacher
# Create your views here.

def get_product_list(request):
    pages = request.GET.get('page', 0)
    objs = ProductModel.objects.all()
    jf = JsonFactory()
    products = jf.makeJsonList(objs, 
            pages,
            'id',
            'title',
            'images',
            'abstract',
            'content',
            'like',
            'share'
        )
    if products:
        return JsonResponse(products, safe=False)
    else:
        return HttpResponse(status=404)


## client 通过商品id获取商品信息。
def get_product_info(request, id):
    obj = ProductModel.objects.filter(id=id)
    if obj:
        obj = obj[0]
        jf = JsonFactory()
        return JsonResponse(jf.makeJson(obj,
            'title',
            'images',
            'abstract',
            'content',
            'like',
            'share'
        ))
    else:
        return HttpResponse(status=404)

####通过商家id按创建时间顺序获得产品
def get_company_product(request, company_id):
    objs = ProductModel.objects.filter(company_id=company_id).order_by('create')
    pages = request.GET.get('page', 0)
    jf = JsonFactory()
    products = jf.makeJsonList(objs, 
        pages,
        'id',
        'images',
        'quantity',
        'price',
        'discount',
        'sales'
    )
    if products:
       return JsonResponse(products, safe=False)
    else:
        return HttpResponse(status=404)


def add_product(request, company_id):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            p = ProductModel()
            p = ObjCacher(p, form, 'title', 'abstract', 'content', 'quantity', 'price', 'discount')
            p.company_id = company_id
            # attrs = ['title', 'abstract', 'content', 'quantity', 'price', 'discount']
            # for attr in attrs:
            #     if form.cleaned_data[attr]:
            #         setattr(p, attr, form.cleaned_data[attr])
            p.save()
            return HttpResponseRedirect('products/show/' + company_id)
        else:
            return JsonResponse({'error': 'form is invalid'})
    form = ProductForm()
    return render(request, 'post.html', {'form': form})
        
## Web
def show_com_pro(request, company_id):
    objs = ProductModel.objects.filter(company_id=company_id)
    titles = ['title', 'abstract', 'content', 'like', 'share', 'sales', 'quantity', 'price', 'discount']
    my_list = make_list(objs, titles)
    cntx = {'titles': titles, 'rows': my_list}
    return render_to_response('CompanyTable.html', cntx)
