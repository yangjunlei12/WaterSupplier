from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from UserInfo.models import UserModel
from UserInfo.UserJsonFactory import UserJsonFactory as JsonFactory
# Create your views here.

def get_num(request):
    if request.method == 'POST':
        num = UserModel.objects.count()
        return JsonResponse({'code': 200, 'data':[{'num': num}]})

def get_vip_num(request):
    if request.method == 'POST':
        num = UserModel.objects.filter(role=1).count()
        return JsonResponse({'code': 200, 'data':[{'num': num}]})


def login(request):
    pass

#### client 
def user_info(request, open_id):
    user = UserModel.objects.filter(open_id=open_id)
    jf = JsonFactory()
    if user:
        user = user[0]
        dict = jf.makeJson(user,
            'phone',
            'age',
            'gender',
            'city',
            'avator',
            'role_name',
            'status'
        )
        return JsonResponse(dict)
    else:
        return HttpResponse(status=404)

def register(request):
    pass