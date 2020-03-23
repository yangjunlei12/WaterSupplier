from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
from Image.models import Img
from WaterSupplier.settings import BASE_DIR
from os.path import join
from io import BytesIO
from urllib.request import urlopen
from time import time
# Create your views here.

def upload_img(request):
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
        return JsonResponse({'code': 200, 'data': [img.img_url.url]})
    return render(request, 'imgupload.html')

def get_img(request):
    url = None
    if request.method == 'GET':
        url = request.GET.get('imgUrl', None)
    if request.method == 'POST':
        url = request.POST.get('imgUrl', None)
    if url:
        image_path = BASE_DIR + url
        # image_path = join(BASE_DIR, url)
        data = None
        img_type = 'image/' + url.split('.')[-1]
        # print(BASE_DIR)
        with open(image_path, 'rb') as img:
            data = img.read()
        if data:
            return HttpResponse(data, content_type=img_type)

### 通过URL上传图片
@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        url = request.POST.get('img', None)
        if url:
            r = urlopen(url)
            io = BytesIO(r.read())
            img = Img()
            
            img.img_url.save('{}.png'.format(int(time())), File(io))
            return JsonResponse({'code': 200, 'data': [img.img_url.url]})
    return JsonResponse({'code': 0, 'msg': '上传失败'})
