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

class OntarioSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class BritishColumbiaSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class QuebecSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class AlbertaSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class SaskatchewanSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class ManitobaSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class NewBrunswickSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class NewfoundlandAndLabradorSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class PrinceEdwardIslandSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class NovaScotiaSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class NorthwestTerritoriesSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class NunavutSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class YukonSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass

class RepatriatedTravellersSerializer(CanadaSerializer):
    class Meta(CanadaSerializer.Meta):
        pass
