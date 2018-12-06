from django.shortcuts import render
from django.http import HttpResponse, request
from django.http.response import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from .models import Post, EnewsPaper, Nuser, ENewsUpload, tinytest
from .forms import ProductForm, RegisterUserForm, UserForm, Userform, UserLoginForm, tinyFormTest, ImageFileUploadForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def home(request):
	all_post = Post.objects.all()

	for post in all_post:
		print(post.title)
		print(post.description)
	return render(request, 'index.html', {'all_post_list': all_post})

def post_list(request):
	post_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		post_list = post_list.filter(title=query)

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
		'regiform':rform
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

# TheENews shows easily runs program
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

#New querry for uploading posts/images & showing by category
def ENewsUploadView(request):
	allENewsInPage = ENewsUpload.objects.all()

	for ENewsUploadView in allENewsInPage:
		print(ENewsUploadView.date)
		print(ENewsUploadView.pageNumber)
		print(ENewsUploadView.position)
		print(ENewsUploadView.category)
		print(ENewsUploadView.news)
	return render(request, 'eNewsDiffer.html', {'singleNews': allENewsInPage})

def eNews(request):
	queryDate = request.GET.get("date")
	queryPage = request.GET.get("p")
	singleNews = ENewsUpload.objects.filter(date=queryDate) | ENewsUpload.objects.filter(pageNumber=queryPage)
	dictionary = {
		'singleNews': singleNews
	}
	return render(request, 'eNewsToday.html', dictionary)

def specific(request):
	# queryCat = request.GET.get("cat")
	queryCat = "education"
	specify = ENewsUpload.objects.filter(category=queryCat)
	return render(request, 'specify.html', {'newsSpecific': specify, 'name':"Joy"})

#User Registration Request
class RegisterUserView(CreateView):
	form_class = RegisterUserForm
	template_name = "templates/registration.html"

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return HttpResponseForbidden()
		
		return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(form.cleaned_data['password'])
		user.save()
		return HttpResponse('User registered')

def Registration(request):
	if request.method=='POST':
		form1 = Userform(request.POST)

		if form1.is_valid():
			username = form1.cleaned_data['username']
			first_name = form1.cleaned_data['first_name']
			last_name = form1.cleaned_data['last_name']
			email = form1.cleaned_data['email']
			password = form1.cleaned_data['password']
			User.objects.create_user(username = username, first_name=first_name, last_name=last_name, email=email, password=password)
			return HttpResponseRedirect('/home/post_list')
	else:
		form1 = Userform()
	return render(request, 'registration.html', {'frm' : form1})

def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return HttpResponseRedirect('/home/post_list')

	return render(request, "login.html", {"loginForm":form})

# ajax using registration
def home(request):
	form = tinyFormTest()
	if request.is_ajax():
		form = tinyFormTest(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			data = {
			'message':'form is saved'
			}
			return JsonResponse(data)
	context = {
	'form':form,
	}
	return render(request,'form.html',context)

def django_image_and_file_upload_ajax(request):
    if request.method == 'POST':
       form = ImageFileUploadForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
       else:
           return JsonResponse({'error': True, 'errors': form.errors})
    else:
        form = ImageFileUploadForm()
        return render(request, 'django_image_upload_ajax.html', {'form': form})