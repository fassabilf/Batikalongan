from django.shortcuts import render, redirect
from event.models import Event
from event.forms import EventForm

def show_event(request):
    events = Event.objects.all()
    return render(request, "event.html", {
        "events": events,
    })

def create_event(request):
    form = EventForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("event:show_event")

    context = { "form": form }
    return render(request, "create_event.html", context)
