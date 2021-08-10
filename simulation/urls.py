from django.urls import path
from .import views

urlpatterns = [
    # path('', views.simulation_form, name='simulation_form'),
    path('simulation/new', views.simulation_form, name='simulation_form'),
    path('simulation/records', views.simulation_records, name='simulation_records'),
    path('simulation/results', views.simulation_results, name='simulation_results'),
]
