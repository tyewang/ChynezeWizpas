from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^translator', include('Translator.urls')),
    url(r'^dashboard', include('UserDashboard.urls')),
    (r'^login/$', 'django.contrib.auth.views.login'),
    # Examples:
    # url(r'^$', 'ChynezeWizpas.views.home', name='home'),
    # url(r'^ChynezeWizpas/', include('ChynezeWizpas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
