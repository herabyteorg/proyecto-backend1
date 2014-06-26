from django.conf.urls import patterns, include, url
from .views import index, test

urlpatterns = patterns('',
   
   # url(r'^$', 'aplicaciones.inicio.views.index' ),
   url(r'^$', index.as_view() ),
   url(r'^test/$', test.as_view() ),
)
