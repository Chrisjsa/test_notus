from django.urls import path
from . import views

urlpatterns = [
    path('simulation/new', views.simulation_form, name='simulation_form'),
    path('simulation/records', views.simulation_records, name='simulation_records'),
    path('simulation/results', views.simulation_results, name='simulation_results'),
    path('simulation/api', views.api_simulation),
    path('simulation/graphics/wt', views.graphics_wt, name='graphics_wt'),
    path('simulation/graphics/tis', views.graphics_tis, name='graphics_tis'),
]
