from django import forms
from .models import *


class SimulationForm(forms.ModelForm):

    class Meta:
        model = Simulation
        fields = ('n_prod_min', 'n_prod_max', 'proc_time', 'replica')
