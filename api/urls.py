from .views import StudentAPIView, HosteliteAPIView
from django.conf.urls import url

urlpatterns = [
        url(r'^student/(?P<usn>[\w]+)/$', StudentAPIView.as_view(), name="stud_ret_view"),
        url(r'^hostelite/(?P<usn>[\w]+)/$', HosteliteAPIView.as_view(), name="host_ret_view")
] 