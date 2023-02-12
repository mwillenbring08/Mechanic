from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('feature.html', views.feature, name="feature"),
    path('project.html', views.project, name="project"),
    path('service.html', views.service, name="service"),
    path('team.html', views.team, name="team"),
    path('testimonial.html', views.testimonial, name="testimonial"),
]

