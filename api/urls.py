from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.get_api_root_view().cls.__doc__ = \
    "You can filter by provinces making requests like: " \
    "\n - http://localhost:8000/api/canada/?prname=Ontario" \
    "\n - http://localhost:8000/api/canada/?prname=British Columbia" \
    "\n " \
    "\n Available provinces are: " \
    "['Ontario', 'British Columbia', 'Canada', 'Quebec', 'Alberta', \
       'Repatriated Travellers', 'Saskatchewan', 'Manitoba', \
       'New Brunswick', 'Newfoundland and Labrador', \
       'Prince Edward Island', 'Nova Scotia', 'Northwest Territories', \
       'Nunavut', 'Yukon', 'Repatriated travellers']" \


router.register('canada', CanadaViewSet)

urlpatterns = [
    path('', include(router.urls))
]