from rest_framework import serializers
from .models import Covid19Ca

Genericfields = (
    'date', 'pruid', 'prname', 'prnameFR', 'numconf', 'numprob','numdeaths',
    'numtotal', 'numtested', 'numrecover', 'percentrecover', 'ratetested',
    'numtoday', 'percentoday'
)

class CanadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19Ca
        fields = Genericfields
