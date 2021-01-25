from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here.

def index(request):
	return render(request, "home.html")

def feedback(request):
	form = FeedbackForm()
	if request.POST:
		form = FeedbackForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Feedback/Query send successfully.')
		else:
			messages.error(request,'Unable to send feedback/query! Please try again later.')
	return redirect('index')

def donationProcess(request):
	return render(request, "dprocess.html")

def aboutUs(request):
	return render(request, "aboutus.html")

def contactUs(request):
	return render(request, "contactus.html")

def gallery(request):
	return render(request, "gallery.html")

def donate(request):
	if not request.session.get('profile_id',None):
		return redirect('login')
	try:
		donor = Donor.objects.get(user=request.session['profile_id'])
	except:
		return redirect('add_doner')
	return render(request, "donate_blood.html")

def addDoner(request):
	if not request.session.get('profile_id',None):
		return redirect('login')
	try:
		donor = Donor.objects.get(user=request.session['profile_id'])
	except:
		donor = None
	if donor:
		return redirect('donate_blood')
	form = DonorForm()
	if request.POST:
		form = DonorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_doner')
	return render(request,"add_donor.html")

def findDoner(request):
	doners = None
	if request.GET.get('blood_group', None) and request.GET.get('location', None):
		doners = Donor.objects.filter(blood_group=request.GET.get('blood_group'),city=request.GET.get('location'))
	return render(request, "find_blood.html", {'doners':doners})
def signup(request):
	if request.session.get('profile_id',None):
		return redirect('index')
	form = ProfileForm()
	if request.POST:
		print(request.POST)
		form = ProfileForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	return render(request,'signup.html', {'form':form})

def login(request):
	if request.session.get('profile_id',None):
		return redirect('index')
	if request.POST:
		print(request.POST)
		email = request.POST.get('email')
		password = request.POST.get('password')
		profile = Profile.objects.get(email=email,password=password)
		request.session['profile_id'] = profile.id
		request.session['profile_name'] = profile.fname+" "+profile.lname
		return redirect('signup')
	return render(request,'login.html')

def logout(request):
	del request.session['profile_id']
	return redirect('index')