from django.shortcuts import render, render_to_response, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from Products.models import ProductModel, ProductType
from Company.models import CompanyModel
from Image.models import Img
from Products.ProductJsonFactory import ProductJsonFactory as JsonFactory
from Products.forms import ProductForm, TypeForm
from django.views.decorators.csrf import csrf_exempt
from utils.ListFactory import make_list
from utils.FormModelSaver import ObjCacher
# Create your views here.

## 后台
@csrf_exempt
def get_product_list(request):
    '''
    post
    '''
    if request.method == 'POST':
        pages = request.POST.get('page', 0)
        company_id = request.POST.get('company_id', 0)
        type_id = request.POST.get('type_id', 0)
        if company_id != 0 and type_id != 0:
            objs = ProductModel.objects.filter(company_id=company_id, type_id=type_id)
        # objs = ProductModel.objects.all()
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
            json = {'code':200, 'data': products}
            return JsonResponse(json)
        else:
            return JsonResponse({'code': 0, 'msg': '未找到符合条件商品'})


## client 通过商品id获取商品信息。
def get_product_info(request):
    if request.method == 'POST':
        id = request.POST.get('id', None)
        if not id:
            return HttpResponse(status=404)
        obj = ProductModel.objects.filter(id=id)
        if obj:
            obj = obj[0]
            jf = JsonFactory()
            json = {'code': 200,
                'data':[jf.makeJson(obj,
                'title',
                'images',
                'abstract',
                'content',
                'like',
                'share'
            )]}
            return JsonResponse(json)
        else:
            return JsonResponse({'code': 0, 'msg': '未找到符合条件商品'})

#### 后台 通过商家id按创建时间顺序获得产品
@csrf_exempt
def get_company_product(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id', None)
        if not company_id:
            return JsonResponse({'code': 0, 'msg': '未找到该商家'})
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
            json = {'code':200, 'data': products}
            return JsonResponse(json)
        else:
            return JsonResponse({'code': 0, 'msg': '未找到符合条件商品'})

@csrf_exempt
def get_product_type(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id', None)
        if not company_id:
            return JsonResponse({'code': 0, 'msg': '未找到该商家'})
        pages = request.GET.get('page', 0)
        objs = ProductModel.objects.filter(company_id=company_id).values_list('type_id', flat=True)
        type_set = list(set(objs))
        type_objs = ProductType.objects.filter(id__in=type_set)
        data = jf.makeJsonList(type_objs, 
            pages,
            'id',
            'company_id',
            'name'
        )
        if data:
            json = {'code': 200, 'data': data}
            return JsonResponse(json)
        else:
            return JsonResponse({'code': 0, 'msg': '未找到符合条件商品'})

### client 获取所以商家的id
def get_company_id(request):
    if request.method == 'POST':
        pages = request.POST.get('pages', 0)
        objs = CompanyModel.objects.all().order_by('member_status')
        jf = JsonFactory()
        companies = jf.makeJsonList(objs,
            pages,
            'id',
        )
        if companies:
            json = {'code':200, 'data': companies}
            return JsonResponse(json)
        else:
            return JsonResponse({'code': 0, 'msg': '未找到公司'})

####  后台 获取所以的商家 按会员级别顺序返回
@csrf_exempt
def all_cqmpanies(request):
    if request.method == 'POST':
        pages = request.POST.get('pages', 0)
        objs = CompanyModel.objects.all().order_by('member_status')
        jf = JsonFactory()
        companies = jf.makeJsonList(objs,
            pages,
            'id',
            'name',
            'logo'
        )
        if companies:
            json = {'code':200, 'data': companies}
            return JsonResponse(json)
        else:
            return JsonResponse({'code': 0, 'msg': '未找到公司'})

## 上传产品照片
@csrf_exempt
def uploadCover(request):
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
        return JsonResponse({'code': 200, 'data': [img.img_url.url]})
    return render(request, 'imgupload.html')

## 后台 上传产品详情图
@csrf_exempt
def upload_detail(request):
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
        return JsonResponse({'code': 200, 'data': [img.img_url.url]})
    return render(request, 'imgupload.html')


@csrf_exempt
def commitProduct(request):
    '''
    post form 参数（均为必填）:
    'company_id': 公司id
    'type_id': 商品种类
    'title': 产品名称
    'images': 轮播图 string
    'abstract': 摘要
    'content': 内容
    'price' : 价格 
    'discount': 折扣

    '''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return JsonResponse({'code': 200, 'message': 'OK'})
        else:
            return JsonResponse({'code': 0, 'message': 'error'})

@csrf_exempt
def add_category(request):
    '''
    post form 参数
    'company_id': 公司id
    'name': 种类的名字
    '''
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return JsonResponse({'code': 200, 'message': 'OK'})
        else:
            return JsonResponse({'code': 0, 'message': 'error'})

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
