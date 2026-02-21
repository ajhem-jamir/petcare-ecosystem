from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment, VeterinaryClinic
from .forms import AppointmentForm

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(pet__owner=request.user).order_by('date', 'time')
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, user=request.user)
        if form.is_valid():
            appointment = form.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('appointments:appointment_list')
    else:
        form = AppointmentForm(user=request.user)
    return render(request, 'appointments/book_appointment.html', {'form': form})

@login_required
def clinic_list(request):
    clinics = VeterinaryClinic.objects.filter(is_active=True)
    return render(request, 'appointments/clinic_list.html', {'clinics': clinics})