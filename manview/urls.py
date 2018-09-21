from django.conf.urls import url
from manview import views
from django.conf import settings
from django.conf.urls.static import static
#necessary imports for the basic working

urlpatterns = [
    url(r'^$', views.index, name = 'manview'),
    url(r'^search/$', views.search, name = 'search'),
    url(r'^detail_view/$', views.detail_view, name="detail_view"),
    url(r'^complaint_update/$',views.complaint_update, name="complaint_update"),
    url(r'^create_pdf/$', views.create_pdf, name = "create_pdf"),
]