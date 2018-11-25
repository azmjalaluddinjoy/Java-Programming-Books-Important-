from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, EnewsPaper, Nuser
from .forms import ProductForm
from .forms import UserForm

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
		rform = UserForm()


	context = {
		'form':form,
		'regiform': rform
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
			'form':form,

		}
		return render(request, 'registration.html', context)

def eNewsView(request):
	allNewsInPage = EnewsPaper.objects.all()

	for eNewsView in allNewsInPage:
		print(eNewsView.date)
		print(eNewsView.pageNumber)
		print(eNewsView.position1)
		print(eNewsView.position2)
		print(eNewsView.position3)
		print(eNewsView.position4)
		print(eNewsView.position5)
		print(eNewsView.position6)
		print(eNewsView.position7)
		print(eNewsView.position8)
		print(eNewsView.position9)
	return render(request, 'eachNewsDiffer.html', {'eachNews': allNewsInPage})

def eachNews(request):
	eachNews = EnewsPaper.objects.all()
	return render(request, 'eNewsPaperHome.html', {'eachNews': eachNews})
