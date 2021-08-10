from django.urls import path
from .import views

urlpatterns = [
    # path('', views.simulation_form, name='simulation_form'),
    path('simulation/new', views.simulation_form, name='simulation_form'),
]
