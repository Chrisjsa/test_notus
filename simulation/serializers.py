from rest_framework import serializers
from .models import *


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulationResult
        fields = ['id', 'avg_wt', 'avg_tis', 'simulation']
