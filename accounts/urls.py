from django.urls import path
from . import views

urlpatterns = [
	path("",views.index, name="index"),
	path("aboutus/",views.aboutUs, name="aboutus"),
	path("gallery/",views.gallery, name="gallery"),
	path("contactus/",views.contactUs, name="contactus"),
	path("donation-process/",views.donationProcess, name="dprocess"),
	path("donate-blood/",views.donate, name="donate_blood"),
	path("find-doner/",views.findDoner, name="find_blood"),
	path("add-doner/",views.addDoner, name="add_doner"),
	path('signup/',views.signup,name='signup'),
	path('login/',views.login,name='login'),
	path('logout/',views.logout,name='logout'),
	path('feedback/',views.feedback,name='feedback'),
]