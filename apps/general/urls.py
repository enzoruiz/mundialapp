from django.conf.urls import patterns, include, url
from .views import InicioView

urlpatterns = patterns('',

    url(r'^$', InicioView.as_view(), name="inicio"),
)
