from django.shortcuts import render, redirect
from .forms import SimulationForm
from .simulation import *

# Create your views here.


def simulation_form(request):
    if request.method == "POST":
        form = SimulationForm(request.POST)
        if form.is_valid():
            simulation = form.save(commit=False)
            # simulation.user = request.user
            # simulation.save()
            run_simulation(request.user,
                           simulation.n_prod_min,
                           simulation.n_prod_max,
                           simulation.proc_time,
                           simulation.replica)
            return redirect('simulation_records')
    else:
        form = SimulationForm()
    return render(request, 'simulation/simulation_form.html', {'form': form})


def simulation_records(request):
    records = Simulation.objects.all()
    return render(request, 'simulation/simulation_records.html', {'records': records})


def simulation_results(request):
    results = SimulationResult.objects.all()
    return render(request, 'simulation/simulation_results.html', {'results': results})
