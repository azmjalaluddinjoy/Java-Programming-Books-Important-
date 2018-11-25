from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='imageNews', blank=True)

	def __str__(self):
		return self.title

class Product(models.Model):
	title 		= models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price		= models.DecimalField(decimal_places=2, max_digits=10000)
	summary		= models.TextField(blank=False, null=False)
	featured	= models.BooleanField(default=False)

	def __str__(self):
		return self.title


class Newusers(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=30)
	address = models.CharField(max_length=100)
	occupation = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=30)

	def __str__(self):
		return self.email

class Nuser(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=30)
	address = models.CharField(max_length=100)
	occupation = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=30)
	image = models.ImageField(upload_to='profile_image', blank=True)

	def __str__(self):
		return self.email

class EnewsPaper(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(max_length=16)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date
