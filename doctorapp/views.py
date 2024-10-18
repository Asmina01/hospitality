from hospitalapp.models import Doctor_hospital
from .forms import *
from django.shortcuts import get_object_or_404, redirect
from .models import Doc_appointment
from django.shortcuts import render


def Appointments(request):
    doctor = request.user.doctor_hospital
    appointments = Doc_appointment.objects.filter(doctor=doctor)
    prescriptions = Patient_prescription.objects.all()
    return render(request, 'doctor/Appointments.html', {'appointments': appointments, 'prescriptions': prescriptions})

def doc_doctorlist(request):

    doctors=Doctor_hospital.objects.all()

    return render(request,'doctor/doc_doctorlist.html',{'doctor':doctors,})

def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Doc_appointment, id=appointment_id)

    if request.method == 'POST':
        prescription_text = request.POST.get('prescription')

        Patient_prescription.objects.update_or_create(
            Appointment=appointment,
            defaults={'Prescription': prescription_text, 'status': 'Completed'}
        )

        return redirect('Appointments')

    return render(request, 'doctor/appointment_detail.html', {'appointment': appointment})


def doctor_add_tip(request):
    if request.method == 'POST':
        form = HealthForm(request.POST)
        if form.is_valid():
            health_tip = form.save(commit=False)

            health_tip.save()
            return redirect('health_tipsview')
    else:
        form = HealthForm()
    return render(request, 'doctor/add_tip.html', {'form': form})


def health_tipsview(request):
    health_tips = Health.objects.all()
    return render(request, 'doctor/health_tipsview.html', {'health_tips': health_tips})


def delete_tip(request, tip_id):
    tip = Health.objects.get(id=tip_id)

    if request.method == "POST":
        tip.delete()
        return redirect("health_tipsview")

    return render(request, 'doctor/delete_tip.html', {'tip': tip})


def doc_dashboard(request):
    doctor = request.user.doctor_hospital

    recent_appointments = Doc_appointment.objects.filter(doctor=doctor).order_by('-created_at')[:5]

    total_appointments = Doc_appointment.objects.filter(doctor=doctor).count()
    completed_appointments = Doc_appointment.objects.filter(doctor=doctor, status='Completed').count()
    pending_appointments = Doc_appointment.objects.filter(doctor=doctor, status='Pending').count()

    context = {
        'doctor': doctor,
        'recent_appointments': recent_appointments,

        'total_appointments': total_appointments,
        'completed_appointments': completed_appointments,
        'pending_appointments': pending_appointments,
    }

    return render(request, 'doc_dashboard.html', context)
