from rest_framework import serializers
from .models import Student,Hostelite

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ("__all__")

class HosteliteSerializer(serializers.ModelSerializer):
    usn = StudentSerializer(required = True)
    class Meta:
        model = Hostelite
        fields = ('usn','keys','counselor','mess_name',)

'''def create(self, validated_data):
        stud_data = validated_data.pop('student')
        usn = StduentSerializer.create(StudentSerializer(), validated_data=stud_data)
        stu, created = Hostelite.objects.update_or_create(usn=usn)
        return stu'''

# class AccountDetailsSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = AccountDetails
# 		fields = ("__all__")

# class AdminSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Admin
# 		fields = ("__all__")

# class ComplaintsSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Complaints
# 		fields = ("__all__")

# class ComplaintFileSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = ComplaintFile
# 		fields = ("__all__")

# class CounselorSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Counselor
# 		fields = ("__all__")

# class EmployeeSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Employee
# 		fields = ("__all__")

# class HostelSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Hostel
# 		fields = ("__all__")

# class KeyPairSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = KeyPair
# 		fields = ("__all__")

# class LocalGuardianSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = LocalGuardian
# 		fields = ("__all__")

# class NonAdminSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = NonAdmin
# 		fields = ("__all__")

# class RoomSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Room
# 		fields = ("__all__")

# class SupervisorSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Supervisor
# 		fields = ("__all__")
		
# class TeacherSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Teacher
# 		fields = ("__all__")