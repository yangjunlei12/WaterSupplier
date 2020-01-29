from django.shortcuts import render, render_to_response
from django.http import JsonResponse, HttpResponse
from Company.models import CompanyModel, ArticleModel
from Company.CmpJsonFactory import CmpJsonFactory as JsonFactory
from utils.ListFactory import make_list
from Company.forms import *
# Create your views here.

####  client 获取所以的商家 按会员级别顺序返回
def all_cqmpanies(request):
    pages = request.GET.get('pages', 0)
    objs = CompanyModel.objects.all().order_by('member_status')
    jf = JsonFactory()
    companies = jf.makeJsonList(objs,
        pages,
        'id',
        'name',
        'logo'
    )
    if companies:
        return JsonResponse(companies, safe=False)
    else:
        return HttpResponse(status=404)

### client 商家动态列表
def get_news(request):
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
        return JsonResponse(news_list, safe=False)
    else:
        return HttpResponse(status=404)

#### client 商家活动列表
def get_activities(request):
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

def add_article(request):
    return render_to_response('post.html', {'form': ArticleForm()})

def test_func(request):
   
    return render(request, 'tables.html')
    # return render_to_response('templates/tables.html', {})