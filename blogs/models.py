from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=120)
	content=models.TextField()
	post_pic=models.ImageField(null=True,blank=True)
	timestamp=models.DateField(auto_now=False,auto_now_add=True)
	


	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title


class Comment(models.Model):
	post=models.ForeignKey(Post,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	comment=models.CharField(max_length=300)
	timestamp=models.DateField(auto_now=False,auto_now_add=True)


	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title







