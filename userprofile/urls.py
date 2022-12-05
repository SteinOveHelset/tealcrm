from django.urls import path

from . import views

app_name = 'userprofile'

urlpatterns = [
    path('myaccount/', views.myaccount, name='myaccount'),
    path('sign-up/', views.signup, name='signup'),
]