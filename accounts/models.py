from django.db import models

# Create your models here.
class Profile(models.Model):
	fname = models.CharField(max_length=15)
	lname = models.CharField(max_length=15)
	dob = models.DateField()
	email = models.EmailField(max_length=30)
	password = models.CharField(max_length=128)

	def __str__(self):
		return (self.fname+' '+self.lname)

class Donor(models.Model):
	user = models.OneToOneField(Profile, on_delete=models.DO_NOTHING)
	contact = models.CharField(max_length=10)
	blood_group = models.CharField(max_length=3)
	address = models.TextField(max_length=100)
	city = models.CharField(max_length=30)
	district = models.CharField(max_length=30)

	def __str__(self):
		return (str(self.user))

class Feedback(models.Model):
	name = models.CharField(max_length=20)
	contact = models.CharField(max_length=10)
	message = models.TextField(100)

	def __str__(self):
		return (self.name)
