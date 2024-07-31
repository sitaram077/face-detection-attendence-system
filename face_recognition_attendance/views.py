# attendance/views.py
from django.shortcuts import render, redirect
from .forms import AttendanceForm
from .models import Attendance

def attendance_list(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')  # Redirect to the list view after saving
    else:
        form = AttendanceForm()

    records = Attendance.objects.all()  # Retrieve all records from the database
    return render(request, 'attendance/attendance_list.html', {'form': form, 'records': records})
