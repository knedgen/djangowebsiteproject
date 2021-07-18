import projects
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def home(request):
    allprojects = Project.objects.all()
    return render(request,'projects/homepage.html', {'allprojects':allprojects})

def project(request):
    return render(request,'projects/projects.html')

def about(request):
    return render(request,'projects/about.html')

def contact(request):
    return render(request,'projects/contact.html')

def pong(request):
    return render(request,'projects/pong.html')