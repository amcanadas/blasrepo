from django.conf.urls import patterns, url
from programacion.views import ProgramacionList

urlpatterns = patterns('',
    url(r'^$', ProgramacionList.as_view(), name='programaciones'),
)