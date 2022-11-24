from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/edit/', views.edit_team, name='edit_team'),
]