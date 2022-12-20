from django.contrib import admin

from .models import Lead, Comment

admin.site.register(Lead)
admin.site.register(Comment)