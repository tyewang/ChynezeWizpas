from django.conf.urls import patterns, url
from Translator import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^/translate', views.translate, name='translate')
)