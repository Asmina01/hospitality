from django.urls import path
from . import views

urlpatterns = [


    path("viewdoctor/",views.viewdoctor, name='viewdoctor'),
    path("base",views.base, name='base'),

    path("facility_userlist/", views.facility_userlist, name='facility_userlist'),
    path("userhealth_tips", views.userhealth_tips, name='userhealth_tips'),
    path('book_appointment/',views.book_appointment, name='book_appointment'),
    path('appointmentlist/',views.appointmentlist, name='appointmentlist'),
    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('user_appointment_detail/<int:appointment_id>/', views.user_appointment_detail, name='user_appointment_detail'),
    path('medical_history/', views.medical_history, name='medical_history'),
    path('create-checkout-session/<int:appointment_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),
    path('payment_page/', views.payment_page, name='payment_page'),


]