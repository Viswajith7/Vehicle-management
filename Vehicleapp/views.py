from django.shortcuts import render,redirect
from Vehicleapp.models import VehicleDB,AdminDB,UserDB
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


# Create your views here.

def index_page(request):
    return render(request,"Index_Page.html")

def Vehicle_Details(request):
    return render(request,"Add_Vehicle_details.html")

def Save_details(request):
    if request.method == "POST":
        vn = request.POST.get("number")
        vt = request.POST.get("type")
        vm = request.POST.get("model")
        vd = request.POST.get("description")
        obj = VehicleDB(Vehicle_Number=vn,Vehicle_Type=vt,Vehicle_Model=vm,Vehicle_Description=vd)
        obj.save()
        return redirect(Vehicle_Details)

def Display_details(request):
    data=VehicleDB.objects.all()
    return render(request,"Display_Vehicle.html",{"data":data})

def Edit_details(request,dataid):
    data = VehicleDB.objects.get(id=dataid)
    return render(request,"Edit_Vehicle.html",{"data":data})


def Update_details(request,dataid):
    if request.method == "POST":
        vn = request.POST.get("number")
        vt = request.POST.get("type")
        vm = request.POST.get("model")
        vd = request.POST.get("description")
        VehicleDB.objects.filter(id=dataid).update(Vehicle_Number=vn,Vehicle_Type=vt,Vehicle_Model=vm,Vehicle_Description=vd)
        return redirect(Display_details)


def Delete_details(request,dataid):
    data = VehicleDB.objects.filter(id=dataid)
    data.delete()
    return redirect(Display_details)


def Super_Adminpage(request):
    return render(request,"Super_Admin.html")

def Superadmin_login(request):
    if request.method == "POST":
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if User.objects.filter(username__contains = username_r).exists():
            user = authenticate(username = username_r,password = password_r)
            if user is not None:
                login(request,user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(index_page)
            else:
                return redirect(Super_Adminpage)
        else:
            return redirect(Super_Adminpage)


def SuperAdminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Super_Adminpage)






def Index_2(request):
    return render(request,"Index2_page.html")


def admin_display(request):
    data=VehicleDB.objects.all()
    return render(request,"Display_Admin.html",{"data":data})

def Edit_admin(req,dataid):
    data = VehicleDB.objects.get(id=dataid)
    return render(req,"Edit_Admin.html",{"data":data})


def Update_admin(req,dataid):
    if req.method == "POST":
        vn = req.POST.get("number")
        vt = req.POST.get("type")
        vm = req.POST.get("model")
        vd = req.POST.get("description")
        VehicleDB.objects.filter(id=dataid).update(Vehicle_Number=vn,Vehicle_Type=vt,Vehicle_Model=vm,Vehicle_Description=vd)
        return redirect(admin_display)



def AdminLoginpage(request):
    return render(request,"Admin_page.html")
def saveadmin(req):
    if req.method == "POST":
        us = req.POST.get("name")
        em = req.POST.get("email")
        ps = req.POST.get("password")
        cps = req.POST.get("cpassword")
        obj = AdminDB(Username=us,Email=em,Password=ps,C_Password=cps)
        obj.save()
        return redirect(AdminLoginpage)
def Adminlogin(request):
    if request.method == "POST":
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if AdminDB.objects.filter(Username=username_r,Password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r

            return redirect(Index_2)
        else:
            return redirect(AdminLoginpage)
    return redirect(AdminLoginpage)
def Admin_Logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(AdminLoginpage)






def Index3(req):
    return render(req,"Index3_page.html")
def Display_user(req):
    data = VehicleDB.objects.all()
    return render(req,"Display_user.html",{"data":data})
def userloginpage(request):
    return render(request,"User_login.html")
def saveuser(req):
    if req.method == "POST":
        us = req.POST.get("name")
        em = req.POST.get("email")
        ps = req.POST.get("password")
        cps = req.POST.get("cpassword")

        obj = UserDB(Username=us,Email=em,Password=ps,C_Password=cps)
        obj.save()
        return redirect(userloginpage)
def Userlogin(request):
    if request.method == "POST":
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if UserDB.objects.filter(Email=username_r,Password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r

            return redirect(Index3)
        else:
            return redirect(userloginpage)
    return redirect(userloginpage)
def User_Logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(userloginpage)