from django.shortcuts import render, redirect
from .models import Event, Volunteer

def home(request):
    return render(request, 'club_app/home.html')


def add_event(request):
    if request.method == "POST":
        Event.objects.create(
            name=request.POST.get('name'),
            date=request.POST.get('date'),
            location=request.POST.get('location')
        )
        return redirect('view_events')
    return render(request, 'club_app/add_event.html')


def view_events(request):
    events = Event.objects.all()
    return render(request, 'club_app/view_events.html', {'events': events})


def volunteer(request):
    if request.method == "POST":
        Volunteer.objects.create(
            name=request.POST.get('name'),
            usn=request.POST.get('usn'),
            event_name=request.POST.get('event_name'),
            availability=request.POST.get('availability')
        )
        return redirect('home')
    return render(request, 'club_app/volunteer.html')


def view_volunteers(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'club_app/view_volunteers.html', {'volunteers': volunteers})