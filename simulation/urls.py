from django.urls import path
from .import views

urlpatterns = [
    path('', views.simulation_form, name='simulation_form')
]