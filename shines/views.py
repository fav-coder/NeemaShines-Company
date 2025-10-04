from django.shortcuts import render,redirect
from django import forms
from .models import Booking, Service

# Create your views here.

def home(request):
    return render(request, 'shines/home.html')
def services(request):
    services = Service.objects.all()
    return render(request, 'shines/services.html', {'services': services})

class ServiceForm(forms.ModelForm):  
    class Meta:
        model = Service
        fields = ['name', 'description', 'image', 'price']
    
    
def service_detail(request, pk):
    service = Service.objects.get(id=pk)
    return render(request, 'shines/service_detail.html', {'service': service})

def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("services")  # Redirect to a service list or confirmation page')
    else:
        form = ServiceForm()
    return render(request, 'shines/services_form.html', {'form': form})   

def update_service(request, pk):
    service_instance = Service.objects.get(id=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service_instance)
        if form.is_valid():
            form.save()
            return redirect("services")  # Redirect to a service list or confirmation page
    else:
        form = ServiceForm(instance=service_instance)
    return render(request, 'shines/services_form.html', {'form': form})

def delete_service(request, pk):
    service_instance = Service.objects.get(id=pk)
    if request.method == 'POST': 
        service_instance.delete()
        return redirect("services")  # Redirect to a service list or confirmation page
    return render(request, 'shines/services_delete.html', {'service': service_instance})   
 
def booking(request):
    form = BookingForm()
    return render(request, 'shines/booking.html',{'form': form  })

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'service', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

#CREATE
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking_list")  # Redirect to a booking list or confirmation page')
    else:
        form = BookingForm()
    return render(request, 'shines/booking_form.html', {'form': form})

#UPDATE
def update_booking(request, pk):
    booking_instance = Booking.objects.get(id=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking_instance)
        if form.is_valid():
            form.save()
            return redirect("booking_list")  # Redirect to a booking list or confirmation page
    else:
        form = BookingForm(instance=booking_instance)
    return render(request, 'shines/booking_form.html', {'form': form})

#DELETE
def delete_booking(request, pk):
   if request.method == 'POST': 
    booking_instance = Booking.objects.get(id=pk)
    booking_instance.delete()
    return redirect("booking_list")  # Redirect to a booking list or confirmation page
   return render(request, 'shines/booking_delete.html', {'booking': booking_instance})

def booking_list(request):
    bookings = Booking.objects.all().order_by("-date")
    return render(request, "shines/booking_list.html", {"bookings": bookings})


def join_us(request):
    return render(request, 'shines/join_us.html')


def contact(request):
    return render(request, 'shines/contact.html')
