from django.conf.urls import *
from aplicaciones.inicio.views import current_datetime, hours_ahead

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Datetime url 
    url(r'^date/$', 'aplicaciones.inicio.views.current_datetime', name='current_datetime'),
    url(r'^date/plus/(\d{1,2})/$', 'aplicaciones.inicio.views.hours_ahead', name='hours_ahead'),
    # url(r'^proyectoA/', include('proyectoA.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
