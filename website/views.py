from django.shortcuts import render

def index(request):
	return render(request, 'index.html', {})

def contact(request):
	return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def feature(request):
	return render(request, 'feature.html', {})

def project(request):
	return render(request, 'project.html', {})

def service(request):
	return render(request, 'service.html', {})

def team(request):
	return render(request, 'team.html', {})

def testimonial(request):
	return render(request, 'testimonial.html', {})
# Create your views here.
