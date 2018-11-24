from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import ProductForm
from .forms import UserForm
from .models import Nuser

# Create your views here.
def home(request):
	all_post = Post.objects.all()

	for post in all_post:
		print(post.title)
		print(post.description)
	return render(request, 'index.html', {'all_post_list': all_post})

def post_list(request):
	post_list = Post.objects.all()
	return render(request, 'post_list.html', {'post_list': post_list})

def single_post(request, post_id):
   post = Post.objects.get(pk=post_id)
   print(post)

   return render(request, 'single_post.html', {'post': post})

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
		regiform = UserForm()


	context = {
		'form':form,
		'regiform': regiform
	}
	return render(request, 'product_create.html', context)

def userRegistration(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = UserForm()

	context = {
		'form':form,
		'regiform': form,
	}
	return render(request, 'registration.html', context)


def userReg(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = UserForm()

		context = {
			'form':form
		}
		return render(request, 'base.html', context)

