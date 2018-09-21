from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from hashlib import sha256
# Create your views here.

def get_server_side_cookie(request, cookie, default_val=None):
    "Return the value of the specified server cookie, return specified value if not found."
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

#creating a cookie user_id, created/updated on login, deleted on logout.
#this is our session management
def index(request):
    
    #if not loggedin, provide the login page.
    user_id = get_server_side_cookie(request,'user_id')
    if user_id==None:
        return render(request, 'login/index.html', {})
    #check if already login, if true, redirect properly
    elif(len(user_id)==10):
        return HttpResponseRedirect('/studview/')
    elif(len(user_id)==7):
        return HttpResponseRedirect('/manview/')
    #Cases done, in anyother case
    else:
        request.session['user_id']=None
        return render(request, 'login/index.html', {})

def check_info(request):
    "NOTE: Exception and shit handling is still pending."
    user = request.POST.get('username')
    passphrase = request.POST.get('pass')
    user_id = (user.upper()).strip()
    pass_id = sha256(passphrase.encode()).hexdigest()
    
    #Student login, create cookie and then redirect
    if(len(user_id)==10):
        #assume name as password, modify if needed later
        with connection.cursor() as cursor:
            cursor.execute("select Fname from STUDENT where USN = %s",[user_id])
            rec = cursor.fetchall()[0][0]
            rec = sha256(rec.encode()).hexdigest()
            if(pass_id == rec):
                #create a cookie
                usn = get_server_side_cookie(request,'user_id')
                if(usn!=user_id or usn==None):
                    request.session['user_id'] = user_id
                    print(get_server_side_cookie(request,'user_id'))
                #redirect to the student sub dom
                return HttpResponseRedirect('/studview/')
            
    elif(len(user_id)==7):
        with connection.cursor() as cursor:
            cursor.execute("select Contact_no from EMPLOYEE where Emp_id = %s AND Designation = 'Supervisor'",[user_id])
            rec = cursor.fetchall()[0][0]
            rec = sha256(rec.encode()).hexdigest()
            if(pass_id == rec):
                #create a cookie
                usn = get_server_side_cookie(request,'user_id')
                if(usn!=user_id or usn==None):
                    request.session['user_id'] = user_id
                    print(get_server_side_cookie(request,'user_id'))
                #redirect to the student sub dom
                return HttpResponseRedirect('/manview/')
    return HttpResponse("<H2>Invalid Login credentials</H2><p>Please check credantial and try again.</p>")

def logout(request):
    "for the logout page."
    request.session['user_id']=None
    return render(request, 'login/logout.html', {})