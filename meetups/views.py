from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    meetups = [
        {"title": 'A First Meetup', 'location': 'New york', 'slug': 'a-first-meetup'},
        {"title": 'A Second Meetup', 'location': 'New jersey', 'slug': 'a-second-meetup'}
    ]
    return render(request, "meetups/index.html",{'meetups':meetups, 'show_meetups': True})

def details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup',
        'location': 'New york',
        'slug': 'a-first-meetup',
        'description': 'this is the selected meetup'
    }

    return render(request, "meetups/details.html", {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description'],
    })