from django.shortcuts import render # render will turn a template to http response
from django.http import HttpResponse # Import HttpResponse for http response return code format
import random # For random numbers
# Create your views here.
def home(request): # Request Response
    return render(request, "password_genarator_app/home.html") # Dictionary key value

def password(request): # Request Response
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('@#$%&!()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # Make length as int
    length = int(request.GET.get('length', 12))

    # Variable for rendering the password
    thePassword = ''

    for x in range(length):
        thePassword+= random.choice(characters)

    return render(request, "password_genarator_app/password.html", {'password':thePassword})

def about(request): # Request Response
    return render(request, "password_genarator_app/about.html") # Dictionary key value
