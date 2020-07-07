from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
	title=models.CharField(max_length=100,null=True,blank=True)
	image=models.ImageField(upload_to='images/')
	summary=models.CharField(max_length=255)


class Profile(models.Model):
	user= models.OneToOneField(User, on_delete=models.CASCADE)
	image=models.ImageField(default='default.png',upload_to='images/profile_pic')

	def __str__(self):
		return f'{self.user.username} Profile'