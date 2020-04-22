from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('canada', CanadaViewSet)
router.register('ontario', OntarioViewSet, basename='ontario')
router.register('british-columbia', BritishColumbiaViewSet,
                basename='british-columbia')
router.register('quebec', QuebecViewSet, basename='quebec')
router.register('alberta', AlbertaViewSet, basename='alberta')
router.register('saskatchewan', SaskatchewanViewSet, basename='saskatchewan')
router.register('manitoba', ManitobaViewSet, basename='manitoba')
router.register('newfoundland-and-labrador', NewfoundlandAndLabradorViewSet,
                basename='newfoundland-and-labrador')
router.register('prince-edward-island', PrinceEdwardIslandViewSet,
                basename='prince-edward-island')
router.register('nova-scotia', NovaScotiaViewSet, basename='nova-scotia')
router.register('northwest-territories', NorthwestTerritoriesViewSet,
                basename='northwest-territories')
router.register('nunavut', NunavutViewSet, basename='nunavut')
router.register('yukon', YukonViewSet, basename='yukon')
router.register('repatriated-travellers', RepatriatedTravellersViewSet,
                basename='repatriated-travellers')

urlpatterns = [
    path('', include(router.urls))
]