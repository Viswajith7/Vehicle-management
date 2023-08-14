from django.urls import path
from Vehicleapp import views

urlpatterns=[
    path('index_page/', views.index_page, name="index_page"),
    path('Vehicle_Details/', views.Vehicle_Details, name="Vehicle_Details"),
    path('Save_details/', views.Save_details, name="Save_details"),
    path('Display_details/', views.Display_details, name="Display_details"),
    path('Edit_details/<int:dataid>/', views.Edit_details, name="Edit_details"),
    path('Update_details/<int:dataid>/', views.Update_details, name="Update_details"),
    path('Delete_details/<int:dataid>/', views.Delete_details, name="Delete_details"),
    path('Super_Adminpage/', views.Super_Adminpage, name="Super_Adminpage"),
    path('SuperAdminLogout/', views.SuperAdminLogout, name="SuperAdminLogout"),
    path('Superadmin_login/', views.Superadmin_login, name="Superadmin_login"),



    path('Index_2/', views.Index_2, name="Index_2"),
    path('admin_display/', views.admin_display, name="admin_display"),
    path('Edit_admin/<int:dataid>/', views.Edit_admin, name="Edit_admin"),
    path('Update_admin/<int:dataid>/', views.Update_admin, name="Update_admin"),
    path('AdminLoginpage/', views.AdminLoginpage, name="AdminLoginpage"),
    path('saveadmin/', views.saveadmin, name="saveadmin"),
    path('Adminlogin/', views.Adminlogin, name="Adminlogin"),
    path('Admin_Logout/', views.Admin_Logout, name="Admin_Logout"),

    path('Index3/', views.Index3, name="Index3"),
    path('Display_user/', views.Display_user, name="Display_user"),
    path('userloginpage/', views.userloginpage, name="userloginpage"),
    path('saveuser/', views.saveuser, name="saveuser"),
    path('Userlogin/', views.Userlogin, name="Userlogin"),
    path('User_Logout/', views.User_Logout, name="User_Logout"),







]
