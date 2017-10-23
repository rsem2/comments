from django.conf.urls import url, include
from . import views

def test(request):
    print "test in app urls"

urlpatterns = [
    url(r'comments/(?P<num>[0-9]+)$', views.profile),
    url(r'submit_comment/(?P<num>[0-9]+)$', views.submit),
    url(r'^$', views.dashboard),
]