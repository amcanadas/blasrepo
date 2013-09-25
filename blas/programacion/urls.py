from django.conf.urls import patterns, url
from programacion.views import ProgramacionList,ProgramacionDetail

urlpatterns = patterns('',
    url(r'^$', ProgramacionList.as_view(), name='programaciones'),
    url(r'^(?P<pk>\d+)/$', ProgramacionDetail.as_view(), name='detalles_programacion'),
)