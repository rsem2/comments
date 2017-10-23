from django.conf.urls import url, include
from . import views

def test(request):
    print "test in app urls"

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^$', views.index),
]

