from django.conf.urls import patterns, url
from normativa.views import MateriaList,MateriaDetail

urlpatterns = patterns('',
    url(r'^$', MateriaList.as_view(), name='modulos'),
    url(r'^(?P<pk>\d+)/$', MateriaDetail.as_view(), name='detalles_modulo'),
)