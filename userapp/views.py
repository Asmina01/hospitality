from django.http import JsonResponse
from django.urls import reverse

from .forms import *
import stripe


from hospitalapp.models import *
from doctorapp.models import *
from userapp.models import patient_Payment

from django.shortcuts import render, redirect, get_object_or_404


def base(request):

    return render(request, 'user/base.html')


def book_appointment(request):
    if request.method == 'POST':
        form = appointmentform(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)

            appointment.user = request.user
            appointment.save()

            return redirect('create_checkout_session', appointment_id=appointment.id)

    else:
        form = appointmentform()

    return render(request, 'user/book_appointment.html', {'form': form})


def appointmentlist(request):

    user = request.user

    appointments = Doc_appointment.objects.filter(user=user)

    return render(request, 'user/appointmentlist.html', {'appointments': appointments})

def delete_appointment(request,appointment_id):

    appointments=Doc_appointment.objects.get(id=appointment_id)

    if request.method=="POST":
        appointments.delete()
        return redirect("appointmentlist")


    return render(request,'user/delete_appointment.html',{'appointments':appointments})


def user_appointment_detail(request, appointment_id):

    appointment = get_object_or_404(Doc_appointment, id=appointment_id, user=request.user)

    try:
        prescription = Patient_prescription.objects.get(Appointment=appointment)
    except Patient_prescription.DoesNotExist:
        prescription = None

    return render(request, 'user/user_appointment_detail.html', {
        'appointment': appointment,
        'prescription': prescription
    })

def viewdoctor(request):

    doctors=Doctor_hospital.objects.all()

    return render(request,'user/viewdoctor.html',{'doctor':doctors,})



def facility_userlist(request):

    facility=Facility.objects.all()

    return render(request,'user/facility_userlist.html',{'facility':facility,})

def userhealth_tips(request):
    health_tips = Health.objects.all()
    return render(request, 'user/userhealth_tips.html', {'health_tips': health_tips})


def medical_history(request):

    completed_appointments = Doc_appointment.objects.filter(
        user=request.user,
        patient_prescription__status="Completed"
    )

    print(f"Found {len(completed_appointments)} completed appointments for user {request.user.username}.")  # Debug info

    medical_history = []
    for appointment in completed_appointments:
        try:
            prescription = appointment.patient_prescription
            medical_history.append({
                'appointment': appointment,
                'prescription': prescription
            })
        except Patient_prescription.DoesNotExist:
            medical_history.append({
                'appointment': appointment,
                'prescription': None
            })

    return render(request, 'user/medical_history.html', {
        'medical_history': medical_history,
    })





def create_checkout_session(request, appointment_id):
    appointment = get_object_or_404(Doc_appointment, id=appointment_id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': f'Consultation with {appointment.doctor.Doc_name}',
                    },
                    'unit_amount': int(250 * 100),
                },
                'quantity': 1,
            }],
            mode='payment',

            success_url=request.build_absolute_uri(reverse("payment_success"))+ '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('payment_cancel'))
        )


        patient_Payment.objects.create(
            appointment=appointment,
            patient=request.user,

            amount=250.00,
            status='success'
        )

        return redirect(session.url, code=303)

    except Exception as e:
        return JsonResponse({'error': str(e)})

def payment_success(request):
    session_id = request.GET.get('session_id')

    return render(request, 'payment_success.html', {'session_id': session_id})

def payment_cancel(request):
    return render(request, 'payment_cancel.html')


def payment_page(request):
    if request.user.is_authenticated:

        payments = patient_Payment.objects.filter(patient=request.user)
    else:
        payments = []

    return render(request, 'user/payment_page.html', {'payments': payments})