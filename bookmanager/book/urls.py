from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(\d+)/(\d+)/', index),
    # url(r'^(?P<value1>\d+)/(?P<value2>\d+)/$', index),
    # 匹配书籍列表信息的URL,调用对应的bookList视图
    url(r'^booklist/$', booklist, name='index'),
    url(r'^testproject/$', testproject, name='test'),
    url(r'^set_cookie/$', set_cookie),
    url(r'^get_cookie/$', get_cookie),
    url(r'^set_session/$', set_session),
    url(r'^get_session/$', get_session),

    url(r'index/$',HomeView.as_view())
]
