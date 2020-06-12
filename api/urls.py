from django.urls import path, include
from rest_framework import routers
from django.utils.safestring import mark_safe
from .views import *

class MyAPIRootView(routers.APIRootView):
    """
    Controls appearance of the API root view
    """
    def get_view_name(self) -> str:
        return "COVID19-CA Rest API"

    def append_link_items(self, pr_name, text, root):
        href = f"{root}{pr_name}"
        text += f"\n <li>" \
                f"\n <a href='{href}'> {pr_name} </a>" \
                f"\n </li>"
        return text

    def get_view_description(self, html=False) -> str:
        prNames = ['Alberta', 'British Columbia', 'Canada', 'Manitoba',
                   'New Brunswick', 'Newfoundland and Labrador',
                   'Northwest Territories', 'Nova Scotia', 'Nunavut',
                   'Ontario', 'Prince Edward Island', 'Quebec',
                   'Repatriated Travellers', 'Saskatchewan', 'Yukon']

        root = "https://covid19-ca.herokuapp.com/api/canada/?prname="

        text = \
            f"This API returns COVID19 statistics for each province in Canada." \
            f"You can filter by provinces using province names on get requests parameters: " \
            f"<ul>" \

        for pr_name in prNames:
            text = self.append_link_items(pr_name, text, root)
        text += f"\n </ul>"

        if html:
            return mark_safe(f"<p>{text}</p>")
        else:
            return text

class MyRouter(routers.DefaultRouter):
    APIRootView = MyAPIRootView

router = MyRouter()


router.register('canada', CanadaViewSet)

urlpatterns = [
    path('', include(router.urls))
]