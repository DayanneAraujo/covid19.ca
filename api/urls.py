from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('canada', CanadaViewSet)
router.register('ontario', OntarioViewSet)
router.register('british-columbia', BritishColumbiaViewSet)
router.register('quebec', QuebecViewSet)
router.register('alberta', AlbertaViewSet)
router.register('saskatchewan', SaskatchewanViewSet)
router.register('manitoba', ManitobaViewSet)
router.register('newfoundland-and-labrador', NewfoundlandAndLabradorViewSet)
router.register('prince-edward-island', PrinceEdwardIslandViewSet)
router.register('nova-scotia', NovaScotiaViewSet)
router.register('northwest-territories', NorthwestTerritoriesViewSet)
router.register('nunavut', NunavutViewSet)
router.register('yukon', YukonViewSet)
router.register('repatriated-travellers', RepatriatedTravellersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]