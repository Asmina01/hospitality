from django.urls import path
from . import views


urlpatterns = [


    path('adminindex/',views.admin_index,name='adminindex'),
    path("doctorform/",views.Create_doctor,name="doctorform"),
    path('doctorlist/',views.doctorlist,name='doctorlist'),

    path('delete_doctor/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
    path('update_doctor/<int:doctor_id>/', views.update_doctor, name='update_doctor'),

    path('update_facility/<int:facility_id>/', views.update_facility, name='update_facility'),
    path("add_facility/",views.add_facility,name="add_facility"),
    path('facility_list/', views.facility_list, name='facility_list'),
    path('delete_facility/<int:facility_id>/', views.delete_facility, name='delete_facility'),

    path('appointment_list/', views.appointment_list, name='appointment_list'),

    path('user_register/', views.user_register, name='user_register'),
    path('', views.user_login, name='login'),
    path('userindex/', views.userindex, name='userindex'),
    path("logout/", views.logout, name="logout"),
    path('register_doctor/', views.register_doctor, name='register_doctor'),


    path('doctorindex/', views.doctorindex, name='doctorindex'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_payment_list/', views.admin_payment_list, name='admin_payment_list'),


]