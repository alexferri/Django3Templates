import random
import string

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from ticketing.models import Ticket

def randomString(stringLenth=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLenth))

def index(request):
    return render(request, "home.html")

def index_jinja(request):
    return render(request, "jinjahome.html")

def showlayout(request):
    return render(request, "applayout.html")


def submit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')
        new_ticket = Ticket(submitter=username, body=body)
        new_ticket.save()
        return HttpResponse("Successfully submitted ticket!")

    return render(request, "submit.html")

def tickets_raw(request):
    all_tickets = list(Ticket.objects.values())
    return JsonResponse(all_tickets, safe=False)

def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request, "tickets.html", {"tickets": all_tickets})

def ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, "ticket.html", {"ticket": ticket})
