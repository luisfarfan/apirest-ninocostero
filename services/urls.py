from .views import *
from django.conf.urls import url
from rest_framework import routers

urlpatterns = [
    url(r'campos/(?P<nivel>[0-9]+)/$', fieldsAmbito.as_view())
]
