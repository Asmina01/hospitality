from django.urls import path
from . import views

urlpatterns = [

    path('doctor/add-tip/', views.doctor_add_tip, name='add_tip'),
    path('health-tipsview/',views.health_tipsview, name='health_tipsview'),
    path('Appointments/', views.Appointments, name='Appointments'),
    path('appointment_detail/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('delete_tip/<int:tip_id>/', views.delete_tip, name='delete_tip'),
    path('doc_dashboard/', views.doc_dashboard, name='doc_dashboard'),
    path('doc_doctorlist/', views.doc_doctorlist, name='doc_doctorlist'),


]