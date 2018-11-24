from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()

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

	def __str__(self):
		return self.email

# class customer(models.Model):
# 	name 		= models.CharField(max_length=120)
# 	description = models.TextField(blank=True, null=True)
# 	roll		= models.DecimalField(decimal_places=2, max_digits=10000)
#
# 	def __str__(self):
# 		return self.title

