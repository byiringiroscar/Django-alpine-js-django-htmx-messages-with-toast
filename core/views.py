from django.shortcuts import render, get_object_or_404
from core.models import Event
from django.contrib import messages

# Create your views here.
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {
        'event': event
    }
    return render(request, 'core/subscribe.html', context)


def subscribe(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.users.add(request.user)
    messages.success(request, f'You have subscribed to Event {event.name}')
    context = {
        'event': event
    }
    response = render(request, 'core/partials/user_li.html', context)
    trigger_client_event(response, 'subscribe', {}) # Trigger the event on the client side to update the UI
    return response

def unsubscribe(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.users.remove(request.user)
    messages.error(request, f'You have unsubscribed from Event {event.name}')
    context = {
        'event': event
    }

    response = render(request, 'core/partials/userlist.html', context)
    trigger_client_event(response, 'subscribe', {})
    return response




from django_htmx.http import trigger_client_event

def count(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {'event': event}
    return render(request, 'core/partials/event_count.html', context)