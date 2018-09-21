from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.conf import settings   

from weasyprint import HTML,CSS
# Create your views here.

def get_server_side_cookie(request, cookie, default_val=None):
    "Return the value of the specified server cookie, return specified value if not found."
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def gen_dict_data(query, complaint_flag = 1):
    "Return a tuple containing one data dictionary and one feild list"
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = dictfetchall(cursor)
        if(complaint_flag==1):
            data = data[0]
        print(data)
        return(data)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def index(request):
    context_dict = {}
    emp_id = get_server_side_cookie(request,'user_id')
    ###### Complaints#####
    if(emp_id==None):
        return HttpResponse("Not logged in.")
    context_dict['user_name'] = emp_id
    
    query = "select Comp_id,Category,Status,Description,Init_timestamp as Filing_timestamp, Update_timestamp from COMPLAINT_FILE where Status!=2"
    context_dict['open_complaint_data']=gen_dict_data(query,0)
    
    query = "select Comp_id,Category,Status,Description,Init_timestamp as Filing_timestamp, Update_timestamp from COMPLAINT_FILE where Status=2"
    context_dict['closed_complaint_data']=gen_dict_data(query,0)
    
    return render(request, 'manview/manview.html', context = context_dict)

def detail_view(request):
    context_dict={}
    u_id = get_server_side_cookie(request,'user_id')
    if(u_id==None):
        return HttpResponse("Not logged in.")
    usn = request.POST.get('USN')
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
    
    ######PARSING COMPLETE####
    return render(request, 'manview/detail_view.html', context = context_dict)

def complaint_update(request):
    'This function is specifically for the updation of the status of the feilds.'
    with connection.cursor() as cursor:
        cursor.execute('select Comp_id from COMPLAINT_FILE where Status!=2')
        data = cursor.fetchall()
        for record in data:
            new_val = request.POST.get("comp_id_"+str(record[0]))
            cursor.execute('update COMPLAINT_FILE set Status = %s where Comp_id = %s',[new_val,record[0]])
    return HttpResponseRedirect('/manview/')

def search(request):
    context_dict = {'students':None, 'columns':None}
    key = request.POST.get('opt')
    print (key)
    
    with connection.cursor() as cursor:
        if key == 'dept':
            dept = request.POST.get('val')
            query = "select * from STUDENT where USN LIKE '_____"+dept+"___'";
            
        elif key == 'usn':
            usn = str(request.POST.get('val'))
            query = "select * from STUDENT where USN ='"+usn+"'";
            
            
        elif key == 'room':
            room = str(request.POST.get('val'))
            print(type(room))
            room_no,block,hostel_id = room.split()
            print(room_no,block,hostel_id)
            query = "select STUDENT.USN,Fname,Lname,Course,Cgpa,Phone_no,Email_id,Address,Gender,ROOM.Room_no from STUDENT,HOSTELITE,HOSTEL,ROOM,KEY_PAIR where STUDENT.USN = HOSTELITE.USN AND HOSTELITE.Keys_id = KEY_PAIR.Cupboard AND KEY_PAIR.Room_id = ROOM.Room_id AND ROOM.Hostel_id = HOSTEL.Hostel_id AND ROOM.Room_no ='"+room_no+"' AND ROOM.Block = '"+block+"' AND ROOM.Hostel_id='"+hostel_id+"'";
            
            
        elif key == 'year':
            year = request.POST.get('val')
            year =18 - int(year)
            query = "select * from STUDENT where USN LIKE '___"+str(year)+"_____'";
            
        cursor.execute(query)
        row = dictfetchall(cursor)
        print(row)    
        context_dict['students'] = row
        context_dict['columns'] = [col[0] for col in cursor.description]
        return render(request, 'manview/search.html', context = context_dict)
    
def create_pdf(request):
    u_id = get_server_side_cookie(request,'user_id')
    if(u_id==None):
        return HttpResponse("Not logged in.")
    usn = request.POST.get('USN')
    print(usn)
    
    # Create the HttpResponse object with the appropriate 
    context_dict = {}
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
    html_string = render_to_string('core/pdf_template.html', context_dict)

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/mypdf.pdf',stylesheets=[CSS(settings.STATIC_ROOT + '/css/w3.css')]);

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s.pdf"'%(usn)
        return response

    return response