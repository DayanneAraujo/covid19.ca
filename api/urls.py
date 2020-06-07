from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
root_url = "domain"
router.get_api_root_view().cls.__doc__ = \
    "You can filter by provinces making requests like:" \
    f'\n - http://{root_url}/api/canada/?prname=Ontario' \
    f'\n - http://{root_url}/api/canada/?prname=British Columbia' \
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