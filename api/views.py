from django.db.models import Q
from rest_framework import generics, mixins
from .models import Student,Hostelite
from .serializers import StudentSerializer,HosteliteSerializer

class StudentAPIView(generics.RetrieveAPIView): #detailview createview formview

	lookup_field		= 'usn' #slug, id# (r'?P<id>\d+')
	serializer_class	= StudentSerializer
	#queryset			= BlogPost.objects.all()

	def get_queryset(self):
		return Student.objects.all()

	# def get_object(self):
	# 	id = self.kwargs.get("id")
	# 	return Student.objects.get(usn = id)

class HosteliteAPIView(generics.RetrieveAPIView): #detailview createview formview

	lookup_field		= 'usn' #slug, id# (r'?P<id>\d+')
	serializer_class	= HosteliteSerializer

	def get_queryset(self):
		return Hostelite.objects.all()