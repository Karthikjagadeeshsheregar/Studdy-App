# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse
from .models import StudyTime, StudyMaterial
from .forms import StudyTimeForm, StudyMaterialForm

# Define a view function for the home page
def home(request):
    return render(request , 'home.html')

# Define a view function for the login page
def login_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username exists
		if not User.objects.filter(username=username).exists():
			# Display an error message if the username does not exist
			messages.error(request, 'Invalid Username')
			return redirect('/login/')
		
		# Authenticate the user with the provided username and password
		user = authenticate(username=username, password=password)
		
		if user is None:
			# Display an error message if authentication fails (invalid password)
			messages.error(request, "Invalid Password")
			return redirect('/login/')
		else:
			# Log in the user and redirect to the home page upon successful login
			login(request, user)
			return redirect('/index/')
	
	# Render the login page template (GET request)
	return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username already exists
		user = User.objects.filter(username=username)
		
		if user.exists():
			# Display an information message if the username is taken
			messages.info(request, "Username already taken!")
			return redirect('/register/')
		
		# Create a new User object with the provided information
		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username
		)
		
		# Set the user's password and save the user object
		user.set_password(password)
		user.save()
		
		# Display an information message indicating successful account creation
		messages.info(request, "Account created Successfully!")
		return redirect('/login/')
	
	# Render the registration page template (GET request)
	return render(request, 'register.html')


def index(request):
    study_times = StudyTime.objects.all()
    study_materials = StudyMaterial.objects.all()
    return render(request, 'index.html', {'study_times': study_times, 'study_materials': study_materials})

def add_study_time(request):
    if request.method == 'POST':
        form = StudyTimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudyTimeForm()
    return render(request, 'studyapp/add_study_time.html', {'form': form})

def delete_study_time(request, pk):
    study_time = StudyTime.objects.get(pk=pk)
    study_time.delete()
    return redirect('index')

def add_material(request):
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        current_url = request.META.get('HTTP_REFERER')
        if form.is_valid():
            form.save()
            return redirect(current_url)
    else:
        form = StudyMaterialForm()
    return render(request, 'studyapp/add_material.html', {'form': form})


def delete_material(request, pk):
    material = StudyMaterial.objects.get(pk=pk)
    material.delete()
    current_url = request.META.get('HTTP_REFERER')
    return redirect(current_url)

def start_study(request):
    study_materials = StudyMaterial.objects.all()
    return render(request, 'studytime.html', { 'study_materials': study_materials})
