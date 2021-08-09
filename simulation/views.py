from django.shortcuts import render

# Create your views here.


def simulation_form(request):
    return render(request, 'simulation/simulation_form.html', {})
