from django.conf.urls import url
from . import views
#url responsible for maping welcome function
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
]
