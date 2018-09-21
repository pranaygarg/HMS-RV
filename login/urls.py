from django.conf.urls import url
from login import views
#necessary imports for the basic working

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^check_info/$', views.check_info, name = 'check_info'),
    url(r'^logout/$', views.logout, name = 'logout'),
]