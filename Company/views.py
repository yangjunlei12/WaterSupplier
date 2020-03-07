from django.shortcuts import render, render_to_response, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Company.models import CompanyModel, ArticleModel
from Image.models import Img
from Company.CmpJsonFactory import CmpJsonFactory as JsonFactory
from utils.ListFactory import make_list
from Company.forms import *
from datetime import datetime
# Create your views here.

####  后台 获取所以的商家 按会员级别顺序返回
@csrf_exempt
def all_cqmpanies(request):
    '''
    post form
        pages
    '''
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
            return JsonResponse({'code': 200, 'data': companies})
        else:
            return JsonResponse({'code': 0, 'msg': 'err '})

## 后台
@csrf_exempt
def get_list(request):
    '''
    post form:
        company_id,
        type_id,
        pages, 
    '''
    if request.method == 'POST':
        company_id = request.POST.get('company_id', None)
        type_id = request.POST.get('type_id', None)
        pages = request.POST.get('pages', 0)
        if company_id != None and type_id != None:
            objs = ArticleModel.objects.filter(company_id=company_id, type_id=type_id)
        else:
            return JsonResponse({'code': 0, 'msg': '未找到符合条件文章'})
        jf = JsonFactory()
        news_list = jf.makeJsonList(objs,
            pages,
            'id',
            'title',
            'abstract',
            'visits',
            'likes',
            'shares'
        )
        if news_list:
            json = {'code':200, 'data': news_list}
            return JsonResponse(json, safe=False)
        else:
            return JsonResponse({'code': 0, 'msg': '未找到符合条件文章'})

## 后台 获得文章种类
@csrf_exempt
def get_categories(request):
    if request.method == 'POST':
        return JsonResponse({'code': 200, 'data': [{'1': '活动', '2': '新闻'}]})

### client 商家动态列表
def get_news(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id', None)
        if not company_id:
            return HttpResponse(status=404)
        pages = request.GET.get('pages', 0)
        objs = ArticleModel.objects.filter(company_id=company_id, type=True)
        jf = JsonFactory()
        news_list = jf.makeJsonList(objs,
            pages,
            'id',
            'title',
            'abstract',
            'visits',
            'likes',
            'shares'
        )
        if news_list:
            json = {'code':200, 'data': news_list}
            return JsonResponse(json, safe=False)
        else:
            return JsonResponse({'code': 0, 'msg': '未找到符合条件文章'})

## 后台 上传封面图片
@csrf_exempt
def uploadCover(request):
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
        return JsonResponse({'code': 200, 'data': [img.img_url.url]})
    return render(request, 'imgupload.html')

## 后台 上传markdown的图片
@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
        return JsonResponse({'code': 200, 'data': [img.img_url.url]})
    return render(request, 'imgupload.html')

## 后台 提交文章
@csrf_exempt
def commitArticle(request):
    '''
    post form = 
        'company_id': ..
        'type_id': ..
        'images': string
        'abstract': string
        'title': string
        'content': string
    
    '''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return JsonResponse({'code': 200})
    return render(request, 'post.html', {'form': ArticleForm()})








#### client 商家活动列表
def get_activities(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id', None)
        if not company_id:
            return HttpResponse(status=404)
        pages = request.GET.get('pages', 0)
        objs = ArticleModel.objects.filter(company_id=company_id, type=False)
        jf = JsonFactory()
        activities = jf.makeJsonList(objs,
            pages,
            'id',
            'title',
            'abstract',
            'visits',
            'likes',
            'shares'
        )
        if activities:
            return JsonResponse(activities, safe=False)
        else:
            return HttpResponse(status=404)

### client 获取类型为活动的文章的数量
def get_activities_count(request):
    count = ArticleModel.objects.filter(type=False).count()
    return JsonResponse({'count': count})


#### client 根据id获取文章
def get_article(request):
    id = request.POST.get('id', None)
    if not id:
        return HttpResponse(status=404)
    obj = ArticleModel.objects.filter(id=id)
    if obj:
        obj = obj[0]
        jf = JsonFactory()
        return JsonResponse(jf.makeJson(obj,
            'id',
            'images',
            'title',
            'content',
            'type',
            'create_time',
            'visits',
            'likes',
            'shares'
        ))
    else:
        return HttpResponse(status=404)

### client 所有的活动
### 未完成 pages 和 轮播图第一页
def get_all_activities(request):
    pages = request.GET.get('pages', 0)
    objs = ArticleModel.objects.filter(type=False).order_by('member_status')
    jf = JsonFactory()
    activities = jf.makeJsonList(objs,
        pages,
        'company_id',
        'id',
        'images',
        'abstract',
        'visits',
        'likes',
        'shares'
    )
    if activities:
        return JsonResponse(activities, safe=False)
    else:
        return HttpResponse(status=404)


def render_table(request):
    objs = CompanyModel.objects.all()
    titles = ['name', 'address', 'logo', 'phone', 'wechat', 'qq', 'member_status']
    my_list = make_list(objs, titles)
    cntx = {'titles': titles, 'rows': my_list}
    return render_to_response('CompanyTable.html', cntx)

def create_com(request):
    return render_to_response('post.html', {'form': CompanyForm()})

@csrf_exempt
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        company_id = request.GET.get('company_id', False)
        print(form.is_valid())
        if form.is_valid() and company_id:
            print('worked here')
            post = form.save(commit=False)
            post.company_id = company_id
            post.visits = 0
            post.likes = 0
            post.shares = 0
            post.create_time = datetime.now()
            print(post)
            post.save()
            return redirect('post_detail', pk=post.pk)

    return render(request, 'post.html', {'form': ArticleForm()})

def test_func(request):
   
    return render(request, 'tables.html')
    # return render_to_response('templates/tables.html', {})