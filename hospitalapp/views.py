from django.contrib import auth
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

from userapp.models import Doc_appointment, patient_Payment

from .forms import *
from hospitalapp.models import Doctor_hospital




def admin_index(request):
    return render(request, 'admin/dashboard.html')

def Create_doctor(request):
    doctor =Doctor_hospital .objects.all()

    if request.method=="POST":
        form=Doctorform(request.POST,files=request.FILES)

        if form.is_valid():
            form.save()

            return redirect("doctorlist")
    else:
        form=Doctorform

    return render(request,"Admin/doctorform.html",{"form":form,"doctor":doctor})

def doctorlist(request):

    doctors=Doctor_hospital.objects.all()

    return render(request,'Admin/doctorlist.html',{'doctor':doctors,})


def delete_doctor(request,doctor_id):

    doctor=Doctor_hospital.objects.get(id=doctor_id)

    if request.method=="POST":
        doctor.delete()
        return redirect("doctorlist")


    return render(request,'admin/delete_doctor.html',{'doctor':doctor})

def update_doctor(request,doctor_id):

    doctor=Doctor_hospital.objects.get(id=doctor_id)
    if request.method=="POST":
        form=Doctorform(request.POST,files=request.FILES,instance=doctor)

        if form.is_valid():
            form.save()
            return redirect("doctorlist")
    else:
        form=Doctorform(instance=doctor)


    return render(request,'Admin/update_doctor.html',{'form':form})


def appointment_list(request):

    appointments = Doc_appointment.objects.all()

    return render(request, 'admin/appointment_list.html', {'appointment_list': appointments})





def facility_list(request):

    facility=Facility.objects.all()

    return render(request,'Admin/facility_list.html',{'facility':facility,})

def add_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm()
    return render(request, 'admin/add_facility.html', {'form': form})

def update_facility(request, facility_id):
    facility = Facility.objects.get(id=facility_id)
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES, instance=facility)
        if form.is_valid():
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm(instance=facility)
    return render(request, 'admin/update_facility.html', {'form': form})

def delete_facility(request,facility_id):

    facility=Facility.objects.get(id=facility_id)

    if request.method=="POST":
        facility.delete()
        return redirect("facility_list")


    return render(request,'admin/delete_facility.html',{'facility':facility})


def userindex(request):

    appointments = Doc_appointment.objects.filter(user=request.user)

    return render(request, 'user/base.html', {'appointments': appointments})
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)


            if user.is_superuser:
                return redirect('adminindex')
            elif hasattr(user, 'doctor_hospital'):
                return redirect('doctorindex')
            else:
                return redirect('userindex')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile.objects.create(user=user)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user_register.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login')


def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data['doc_username'],
                password=form.cleaned_data['password']
            )

            doctor_profile = form.save(commit=False)
            doctor_profile.user = user
            doctor_profile.save()
            return redirect('doctorlist')
    else:
        form = DoctorRegistrationForm()

    return render(request, 'admin/register_doctor.html', {'form': form})


def doctorindex(request):

    doctor = Doctor_hospital.objects.get(user=request.user)


    return render(request, 'doctor/doc_dashboard.html', {'doctor': doctor})




def dashboard(request):
    total_appointments = len(Doc_appointment.objects.all())
    total_patients = len(User.objects.filter(is_patient=True))
    recent_appointments = Doc_appointment.objects.order_by('-created_at')[:5]

    context = {

        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'recent_appointments': recent_appointments,

    }

    return render(request, 'dashboard.html', context)

def admin_payment_list(request):
    payments = patient_Payment.objects.all()
    context = {
        'payments': payments
    }
    return render(request, 'admin/admin_payment_list.html', context)





