#TODO: level 1 - Recognising current status of mental health and provide steps accordingly to prevent problems ML model to predict Mental degradation and provide steps accordingly
#TODO: A portal where therapists and people can sign up and people can book appointments with therapists
#TODO: UI - A autism, color blindness, epilepsy friendly
#TODO: Think and ideate for level 2 - software support for fighting mental health


from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
	return render(request, "home.html")

def login(request):
	return render(request,'login.html')

def signup(request):
	
	return render(request,'signup.html')