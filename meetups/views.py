from django.shortcuts import render


# Create your views here.
def index(request):
    meetups = [
        {"title": 'A First Meetup', 'location': 'New york', 'slug': 'a-first-meetup'},
        {"title": 'A Second Meetup', 'location': 'New jersey', 'slug': 'a-second-meetup'}
    ]
    return render(request, "meetups/index.html",{'meetups':meetups, 'show_meetups': True})