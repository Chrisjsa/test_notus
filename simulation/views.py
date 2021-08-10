from django.shortcuts import render, redirect
from .forms import SimulationForm
from .simulation import run_simulation

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
            return redirect('simulation_records', pk=simulation.pk)
    else:
        form = SimulationForm()
    return render(request, 'simulation/simulation_form.html', {'form': form})
