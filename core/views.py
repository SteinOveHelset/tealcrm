from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')