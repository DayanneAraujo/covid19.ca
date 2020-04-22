from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response

class CanadaViewSet(viewsets.ModelViewSet):
    queryset = Covid19Ca.objects.all()
    serializer_class = CanadaSerializer

    def update(self, request, *args, **kwargs):
        response = {'message': 'You are not allowed to update.' }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You are not allowed to insert data.'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You are not allowed to delete content.'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class OntarioViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Ontario')
    serializer_class = OntarioSerializer

class BritishColumbiaViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='British Columbia')
    serializer_class = BritishColumbiaSerializer

class QuebecViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Quebec')
    serializer_class = QuebecSerializer

class AlbertaViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Alberta')
    serializer_class = AlbertaSerializer

class SaskatchewanViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Saskatchewan')
    serializer_class = SaskatchewanSerializer

class ManitobaViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Manitoba')
    serializer_class = ManitobaSerializer

class NewBrunswickViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='New Brunswick')
    serializer_class = NewBrunswickSerializer

class NewfoundlandAndLabradorViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Newfoundland and Labrador')
    serializer_class = NewfoundlandAndLabradorSerializer

class PrinceEdwardIslandViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Prince Edward Island')
    serializer_class = PrinceEdwardIslandSerializer

class NovaScotiaViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Nova Scotia')
    serializer_class = NovaScotiaSerializer

class NorthwestTerritoriesViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Northwest Territories')
    serializer_class = NorthwestTerritoriesSerializer

class NunavutViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Nunavut')
    serializer_class = NunavutSerializer

class YukonViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Yukon')
    serializer_class = YukonSerializer

class RepatriatedTravellersViewSet(CanadaViewSet):
    queryset = Covid19Ca.objects.filter(prname='Repatriated Travellers')
    serializer_class = RepatriatedTravellersSerializer
