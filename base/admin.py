from django.contrib import admin
from .models import User,Blogge,Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Blogge)
admin.site.register(Comment)

