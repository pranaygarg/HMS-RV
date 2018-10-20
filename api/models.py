# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `#managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountDetails(models.Model):
    usn = models.ForeignKey('Hostelite', models.DO_NOTHING, db_column='USN', primary_key=True)  # Field name made lowercase.
    prev_bal = models.IntegerField(db_column='Prev_bal', blank=True, null=True)  # Field name made lowercase.
    cur_bal = models.IntegerField(db_column='Cur_bal', blank=True, null=True)  # Field name made lowercase.
    no_of_days_eaten = models.IntegerField(db_column='No_of_days_eaten', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ACCOUNT_DETAILS'


class Admin(models.Model):
    emp = models.ForeignKey('Employee', models.DO_NOTHING, db_column='Emp_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ADMIN'


class Complaints(models.Model):
    category = models.CharField(db_column='Category', primary_key=True, max_length=15)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'COMPLAINTS'


class ComplaintFile(models.Model):
    comp_id = models.AutoField(db_column='Comp_id', primary_key=True)  # Field name made lowercase.
    usn = models.ForeignKey('Hostelite', models.DO_NOTHING, db_column='USN', blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(Complaints, models.DO_NOTHING, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    init_timestamp = models.DateTimeField(db_column='Init_timestamp')  # Field name made lowercase.
    update_timestamp = models.DateTimeField(db_column='Update_timestamp')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'COMPLAINT_FILE'


class Counselor(models.Model):
    t = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='T_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'COUNSELOR'


class Employee(models.Model):
    emp_id = models.CharField(db_column='Emp_id', primary_key=True, max_length=7)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    contact_no = models.CharField(db_column='Contact_no', max_length=10, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'EMPLOYEE'


class Hostel(models.Model):
    hostel_id = models.IntegerField(db_column='Hostel_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    floors = models.IntegerField(db_column='Floors', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'HOSTEL'


class Hostelite(models.Model):
    usn = models.ForeignKey('Student', models.DO_NOTHING, db_column='USN', primary_key=True, related_name = 'hostelite')  # Field name made lowercase.
    keys = models.ForeignKey('KeyPair', models.DO_NOTHING, db_column='Keys_id', blank=True, null=True)  # Field name made lowercase.
    counselor = models.ForeignKey(Counselor, models.DO_NOTHING, db_column='Counselor_id', blank=True, null=True)  # Field name made lowercase.
    mess_name = models.ForeignKey('Mess', models.DO_NOTHING, db_column='Mess_name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'HOSTELITE'


class KeyPair(models.Model):
    cupboard = models.IntegerField(db_column='Cupboard', primary_key=True)  # Field name made lowercase.
    door = models.IntegerField(db_column='Door', blank=True, null=True)  # Field name made lowercase.
    locker1 = models.IntegerField(db_column='Locker1', blank=True, null=True)  # Field name made lowercase.
    locker2 = models.IntegerField(db_column='Locker2', blank=True, null=True)  # Field name made lowercase.
    room = models.ForeignKey('Room', models.DO_NOTHING, db_column='Room_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'KEY_PAIR'


class LocalGuardian(models.Model):
    usn = models.ForeignKey(Hostelite, models.DO_NOTHING, db_column='USN', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    relation = models.CharField(db_column='Relation', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone_no = models.CharField(db_column='Phone_no', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_id', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LOCAL_GUARDIAN'


class Mess(models.Model):
    mess_name = models.CharField(db_column='Mess_name', primary_key=True, max_length=10)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.
    menu = models.TextField(db_column='Menu', blank=True, null=True)  # Field name made lowercase.
    hostel = models.ForeignKey(Hostel, models.DO_NOTHING, db_column='Hostel_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'MESS'


class NonAdmin(models.Model):
    emp = models.ForeignKey(Employee, models.DO_NOTHING, db_column='Emp_id', primary_key=True)  # Field name made lowercase.
    hostel = models.ForeignKey(Hostel, models.DO_NOTHING, db_column='Hostel_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'NON_ADMIN'


class Room(models.Model):
    room_id = models.IntegerField(db_column='Room_id', primary_key=True)  # Field name made lowercase.
    room_no = models.IntegerField(db_column='Room_no', blank=True, null=True)  # Field name made lowercase.
    block = models.CharField(db_column='Block', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hostel = models.ForeignKey(Hostel, models.DO_NOTHING, db_column='Hostel_id', blank=True, null=True)  # Field name made lowercase.
    students = models.IntegerField(db_column='Students', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ROOM'


class Student(models.Model):
    usn = models.CharField(db_column='USN', primary_key=True, max_length=10)  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=15)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=15)  # Field name made lowercase.
    course = models.CharField(db_column='Course', max_length=10)  # Field name made lowercase.
    cgpa = models.DecimalField(db_column='Cgpa', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    phone_no = models.CharField(db_column='Phone_no', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_id', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'STUDENT'
        
    def __str__(self):
        return self.usn


class Supervisor(models.Model):
    hostel = models.ForeignKey(Hostel, models.DO_NOTHING, db_column='Hostel_id', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey(Admin, models.DO_NOTHING, db_column='Emp_id')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'SUPERVISOR'
        unique_together = (('hostel', 'emp'),)


class Teacher(models.Model):
    t_id = models.CharField(db_column='T_id', primary_key=True, max_length=7)  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mob_no = models.CharField(db_column='Mob_no', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_id', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'TEACHER'