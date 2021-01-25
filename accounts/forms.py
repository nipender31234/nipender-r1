from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth import password_validation

class ProfileForm(ModelForm):
	password = forms.CharField(
			widget=forms.PasswordInput,
			help_text=password_validation.password_validators_help_text_html(),
		)
	cpassword = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Profile 
		fields = ['fname','lname','dob','email','password']
	def clean(self):
		clean_data = super(ProfileForm,self).clean()
		password = clean_data.get('password')
		cpassword = clean_data.get('cpassword')
		if password != cpassword:
			raise forms.ValidationError('password & cpassword does not matched')
		password_validation.validate_password(cpassword,self)

class DonorForm(ModelForm):
	class Meta:
		model = Donor
		fields = ['user','contact','blood_group','address','city','district']

class FeedbackForm(ModelForm):
	class Meta:
		model = Feedback
		fields = ['name','contact','message']