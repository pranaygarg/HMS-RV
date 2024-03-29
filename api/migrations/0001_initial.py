# Generated by Django 2.1.2 on 2018-10-20 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintFile',
            fields=[
                ('comp_id', models.AutoField(db_column='Comp_id', primary_key=True, serialize=False)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=150, null=True)),
                ('init_timestamp', models.DateTimeField(db_column='Init_timestamp')),
                ('update_timestamp', models.DateTimeField(db_column='Update_timestamp')),
            ],
            options={
                'db_table': 'COMPLAINT_FILE',
            },
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('category', models.CharField(db_column='Category', max_length=15, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'COMPLAINTS',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(db_column='Emp_id', max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=25, null=True)),
                ('contact_no', models.CharField(blank=True, db_column='Contact_no', max_length=10, null=True)),
                ('designation', models.CharField(blank=True, db_column='Designation', max_length=15, null=True)),
            ],
            options={
                'db_table': 'EMPLOYEE',
            },
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('hostel_id', models.IntegerField(db_column='Hostel_id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=10, null=True)),
                ('floors', models.IntegerField(blank=True, db_column='Floors', null=True)),
            ],
            options={
                'db_table': 'HOSTEL',
            },
        ),
        migrations.CreateModel(
            name='KeyPair',
            fields=[
                ('cupboard', models.IntegerField(db_column='Cupboard', primary_key=True, serialize=False)),
                ('door', models.IntegerField(blank=True, db_column='Door', null=True)),
                ('locker1', models.IntegerField(blank=True, db_column='Locker1', null=True)),
                ('locker2', models.IntegerField(blank=True, db_column='Locker2', null=True)),
            ],
            options={
                'db_table': 'KEY_PAIR',
            },
        ),
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('mess_name', models.CharField(db_column='Mess_name', max_length=10, primary_key=True, serialize=False)),
                ('capacity', models.IntegerField(blank=True, db_column='Capacity', null=True)),
                ('menu', models.TextField(blank=True, db_column='Menu', null=True)),
            ],
            options={
                'db_table': 'MESS',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(db_column='Room_id', primary_key=True, serialize=False)),
                ('room_no', models.IntegerField(blank=True, db_column='Room_no', null=True)),
                ('block', models.CharField(blank=True, db_column='Block', max_length=1, null=True)),
                ('students', models.IntegerField(blank=True, db_column='Students', null=True)),
            ],
            options={
                'db_table': 'ROOM',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('usn', models.CharField(db_column='USN', max_length=10, primary_key=True, serialize=False)),
                ('fname', models.CharField(db_column='Fname', max_length=15)),
                ('lname', models.CharField(db_column='Lname', max_length=15)),
                ('course', models.CharField(db_column='Course', max_length=10)),
                ('cgpa', models.DecimalField(blank=True, db_column='Cgpa', decimal_places=2, max_digits=4, null=True)),
                ('phone_no', models.CharField(blank=True, db_column='Phone_no', max_length=10, null=True)),
                ('email_id', models.CharField(blank=True, db_column='Email_id', max_length=40, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=100, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=6, null=True)),
            ],
            options={
                'db_table': 'STUDENT',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('t_id', models.CharField(db_column='T_id', max_length=7, primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, db_column='Fname', max_length=10, null=True)),
                ('lname', models.CharField(blank=True, db_column='Lname', max_length=10, null=True)),
                ('mob_no', models.CharField(blank=True, db_column='Mob_no', max_length=10, null=True)),
                ('email_id', models.CharField(blank=True, db_column='Email_id', max_length=60, null=True)),
            ],
            options={
                'db_table': 'TEACHER',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('emp', models.ForeignKey(db_column='Emp_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.Employee')),
            ],
            options={
                'db_table': 'ADMIN',
            },
        ),
        migrations.CreateModel(
            name='Counselor',
            fields=[
                ('t', models.ForeignKey(db_column='T_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.Teacher')),
            ],
            options={
                'db_table': 'COUNSELOR',
            },
        ),
        migrations.CreateModel(
            name='Hostelite',
            fields=[
                ('usn', models.ForeignKey(db_column='USN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.Student')),
            ],
            options={
                'db_table': 'HOSTELITE',
            },
        ),
        migrations.CreateModel(
            name='NonAdmin',
            fields=[
                ('emp', models.ForeignKey(db_column='Emp_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.Employee')),
            ],
            options={
                'db_table': 'NON_ADMIN',
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('hostel', models.ForeignKey(db_column='Hostel_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.Hostel')),
                ('type', models.CharField(blank=True, db_column='Type', max_length=30, null=True)),
                ('emp', models.ForeignKey(db_column='Emp_id', on_delete=django.db.models.deletion.DO_NOTHING, to='api.Admin')),
            ],
            options={
                'db_table': 'SUPERVISOR',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='hostel',
            field=models.ForeignKey(blank=True, db_column='Hostel_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Hostel'),
        ),
        migrations.AddField(
            model_name='mess',
            name='hostel',
            field=models.ForeignKey(blank=True, db_column='Hostel_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Hostel'),
        ),
        migrations.AddField(
            model_name='keypair',
            name='room',
            field=models.ForeignKey(blank=True, db_column='Room_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Room'),
        ),
        migrations.AddField(
            model_name='complaintfile',
            name='category',
            field=models.ForeignKey(blank=True, db_column='Category', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Complaints'),
        ),
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('usn', models.ForeignKey(db_column='USN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.Hostelite')),
                ('prev_bal', models.IntegerField(blank=True, db_column='Prev_bal', null=True)),
                ('cur_bal', models.IntegerField(blank=True, db_column='Cur_bal', null=True)),
                ('no_of_days_eaten', models.IntegerField(blank=True, db_column='No_of_days_eaten', null=True)),
            ],
            options={
                'db_table': 'ACCOUNT_DETAILS',
            },
        ),
        migrations.CreateModel(
            name='LocalGuardian',
            fields=[
                ('usn', models.ForeignKey(db_column='USN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.Hostelite')),
                ('fname', models.CharField(blank=True, db_column='Fname', max_length=20, null=True)),
                ('relation', models.CharField(blank=True, db_column='Relation', max_length=10, null=True)),
                ('phone_no', models.CharField(blank=True, db_column='Phone_no', max_length=10, null=True)),
                ('email_id', models.CharField(blank=True, db_column='Email_id', max_length=40, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=100, null=True)),
                ('lname', models.CharField(blank=True, db_column='Lname', max_length=20, null=True)),
            ],
            options={
                'db_table': 'LOCAL_GUARDIAN',
            },
        ),
        migrations.AddField(
            model_name='nonadmin',
            name='hostel',
            field=models.ForeignKey(blank=True, db_column='Hostel_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Hostel'),
        ),
        migrations.AddField(
            model_name='hostelite',
            name='counselor',
            field=models.ForeignKey(blank=True, db_column='Counselor_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Counselor'),
        ),
        migrations.AddField(
            model_name='hostelite',
            name='keys',
            field=models.ForeignKey(blank=True, db_column='Keys_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.KeyPair'),
        ),
        migrations.AddField(
            model_name='hostelite',
            name='mess_name',
            field=models.ForeignKey(blank=True, db_column='Mess_name', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mess'),
        ),
        migrations.AddField(
            model_name='complaintfile',
            name='usn',
            field=models.ForeignKey(blank=True, db_column='USN', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Hostelite'),
        ),
        migrations.AlterUniqueTogether(
            name='supervisor',
            unique_together={('hostel', 'emp')},
        ),
    ]
