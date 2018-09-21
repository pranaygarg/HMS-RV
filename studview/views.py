from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
# Create your views here.

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
def gen_dict_data(query, complaint_flag = 1):
    "Return a tuple containing one data dictionary and one feild list"
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = dictfetchall(cursor)
        if(complaint_flag==1):
            data = data[0]
        print(data)
        return(data)

def index(request):
    context_dict={}
    usn = get_server_side_cookie(request,'user_id')
    if(usn==None):
        return HttpResponse("Not logged in.")
    
    ######STUD######
    query = "select * from STUDENT natural join HOSTELITE where USN = '"+usn+"'"
    context_dict['stud_data']=gen_dict_data(query)
    context_dict['user_name'] = context_dict['stud_data']['Fname']
    
    ######Room Data###
    query = "select Name as Hostel_Name,Room_no,Block, Door as Door_key, Cupboard as Cupboard_key from HOSTELITE,HOSTEL,ROOM,KEY_PAIR where HOSTELITE.Keys_id = KEY_PAIR.Cupboard AND KEY_PAIR.Room_id = ROOM.Room_id AND ROOM.Hostel_id = HOSTEL.Hostel_id AND USN = '"+usn+"'"
    context_dict['room_data']=gen_dict_data(query)
    
    ######Counselor Info###
    query = "select TEACHER.* from TEACHER,HOSTELITE where HOSTELITE.Counselor_id = TEACHER.T_id AND USN = '"+usn+"'"
    context_dict['counselor_data']=gen_dict_data(query)
    
    #####Guardian Info####
    query = "select Fname,Lname,Relation,Phone_no,Email_id,Address from LOCAL_GUARDIAN where USN = '"+usn+"'"
    context_dict['guardian_data']=gen_dict_data(query)
    
    ###### Complaints#####
    query = "select Comp_id,Category,Status,Description,Init_timestamp as Filing_timestamp, Update_timestamp from COMPLAINT_FILE where USN = '"+usn+"'"
    context_dict['complaint_data']=gen_dict_data(query,0)
    
    ###NOTE: FILING OF COMPLAINT STILL LEFT.####
    ####Mess Info View######
    query = "select HOSTELITE.Mess_name,Menu,Cur_bal as Mess_balance, No_of_days_eaten as DAY_COUNT from MESS,HOSTELITE,ACCOUNT_DETAILS where MESS.Mess_name=HOSTELITE.Mess_name AND ACCOUNT_DETAILS.USN = HOSTELITE.USN AND HOSTELITE.USN = '"+usn+"'"
    context_dict['mess_data']=gen_dict_data(query)
    #########################
    
    #####Fectching all categories of complaints#####
    query = "select * from COMPLAINTS"
    data = None
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = dictfetchall(cursor)
    context_dict['category'] = data
    print(data)
    
    ######PARSING COMPLETE####
    return render(request, 'studview/studview.html', context = context_dict)

def complaint_reg(request):
    usn = get_server_side_cookie(request,'user_id')
    if(usn==None):
        return HttpResponse("Not logged in.")
    category = request.POST.get('category')
    description = request.POST.get('description')
    with connection.cursor() as cursor:
        cursor.execute("insert into COMPLAINT_FILE (USN,Category,Description) values(%s,%s,%s)",[usn,category,description])
    return HttpResponseRedirect("/studview/")