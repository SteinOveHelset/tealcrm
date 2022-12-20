from django.contrib import admin

from .models import Client, Comment

admin.site.register(Client)
admin.site.register(Comment)