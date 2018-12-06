from django.contrib import admin
# from blog_post.models import Post
# erokokm lekhar proyojon nai. 
# Onno kono app er model import korte hole app_name.models
# r ek e app er model import korte hole .models import class_name dilei chole
from .models import Post
from .models import Product
from .models import Nuser
from .models import EnewsPaper
from .models import ENewsUpload
from .models import tinytest

# Register your models here.
admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Nuser)
admin.site.register(EnewsPaper)
admin.site.register(ENewsUpload)
admin.site.register(tinytest)
admin.site.site_header = "The SoftTech Bangladesh E-Newspaper Administration"
admin.site.site_title = "The SoftTech Bangladesh E-Newspaper Admin Portal"
admin.site.index_title = "Welcome to The SoftTech Bangladesh Portal"