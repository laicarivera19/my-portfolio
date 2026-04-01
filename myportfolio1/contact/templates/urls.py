from django.urls import path
from  project import views


urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('', include('main.urls')),
]