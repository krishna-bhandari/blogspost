from django.db import models

# Create your models here.
class Blog(models.Model):
	title=models.CharField(max_length=255)
	pub_date=models.DateTimeField()
	image=models.ImageField(upload_to='images/')
	body=models.TextField()

	def date_only(self):
		return(self.pub_date.strftime('%b %e, %y'))
	def body_summary(self):
		return(self.body[0:100])
	def __str__(self):
		return(self.title)
	
