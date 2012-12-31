from django.conf.urls import patterns, url
from UserDashboard import views

urlpatterns = patterns('',
       url(r'^$', views.main, name='main'),
)