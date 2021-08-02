import json
from django.shortcuts import render
from django.http import HttpResponse, request, response
from .models import BookInfo, PersonInfo
from django.urls import reverse
from datetime import datetime


# Create your views here.

def index(request, value1, value2):
    # context = {'title': '测试模板数据'}
    # return render(request, 'book/index.html', context)
    # context = {'v1': value1, 'v2': value2}
    # print(context)
    # return render(request, 'book/index.html', context)

    '''请求头'''
    CONTENT_TYPE = request.META['CONTENT_TYPE']
    print(CONTENT_TYPE)
    return HttpResponse('OKK!')


def booklist(requset):
    # books = BookInfo.objects.all()
    # context = {'books': books}
    # return render(requset, 'book/booklist.html', context)
    url = reverse('book:index')
    print(url)
    return HttpResponse('index')


def testproject(request):
    return HttpResponse('OK')


def set_cookie(request):
    username = request.GET.get('username')
    response = HttpResponse('第一次set_cookie')
    response.set_cookie('username', username, max_age=3600)
    return response


def get_cookie(request):
    cookie = request.COOKIES
    username = cookie.get('username')
    print(username)
    return HttpResponse('第二次get_cookie')


def set_session(requset):
    print(requset.COOKIES)
    user_id = 666
    requset.session['user_id'] = user_id
    return HttpResponse('set_session')


def get_session(requset):
    print(requset.COOKIES)
    user_id = requset.session['user_id']
    print(user_id)
    return HttpResponse('get_session')


#############################模板############################################

from django.views import View


class HomeView(View):
    def get(self, request):
        # 1.获取数据
        username = request.GET.get('username')

        # 2.组织数据
        context = {
            'username': username,
            'age': 14,
            'birthday': datetime.now(),
            'firends': ['tom', 'jack', 'rose'],
            'money': {
                '2019': 12000,
                '2020': 18000,
                '2021': 25000,
            },
            'desc': '<script>alert("hot")</script>'
        }

        # return render(request,'detail.html')
        return render(request, 'index.html', context=context)
