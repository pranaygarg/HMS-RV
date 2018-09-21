from django.conf.urls import url
from studview import views
#necessary imports for the basic working

urlpatterns = [
    url(r'^$', views.index, name = 'studview'),
    url(r'^complaint_reg/$', views.complaint_reg, name="complaint_reg"),
]