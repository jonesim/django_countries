from django.urls import path

from .views import CountryList

urlpatterns = [
    path('country-list/', CountryList.as_view(), name='countries'),
]
