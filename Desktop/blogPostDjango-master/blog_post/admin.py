from django.contrib import admin
# from blog_post.models import Post
# erokokm lekhar proyojon nai. 
# Onno kono app er model import korte hole app_name.models
# r ek e app er model import korte hole .models import class_name dilei chole
from .models import Post
from .models import Product

# Register your models here.
admin.site.register(Post)
admin.site.register(Product)
