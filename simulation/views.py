from django.shortcuts import render, redirect
from .forms import SimulationForm
from .simulation import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ResultsSerializer


def simulation_form(request):
    if request.method == "POST":
        form = SimulationForm(request.POST)
        if form.is_valid():
            simulation = form.save(commit=False)
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


@api_view(['POST'])
def api_simulation(request):
    data = request.data
    run_simulation(request.user, data['n_prod_min'], data['n_prod_max'], data['proc_time'], data['replica'])
    queryset = SimulationResult.objects.all()
    serializer = ResultsSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
