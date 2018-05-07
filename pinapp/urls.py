'''To design URLs for an app, you create a Python module informally called a URLconf (URL configuration).
 This module is pure Python code and is a mapping between URL path expressions to Python functions (your views).
 '''
from django.conf.urls import url
from . import views
from django.conf import settings


#url responsible for maping welcome function
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)', views.image, name='image'),
]
