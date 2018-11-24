from django.urls import path
from . import views
 
urlpatterns = [
	path('home/', views.home, name = 'blog_home'),
    path('post_list/', views.post_list, name ='post_list'),
    path ('create/', views.product_create_view, name='product_create_view'),
    path ('new_user/', views.userRegistration, name='userRegistration'),
    path ('reg/', views.userReg, name='userRegistration'),
    path('single_post/<post_id>/', views.single_post, name='single_post'),
]
