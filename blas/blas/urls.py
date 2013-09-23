from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blas.views.home', name='home'),
    # url(r'^blas/', include('blas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
    url(r'^admin/', include(admin.site.urls),name='admin'),

    url(r'^normativa/', include('normativa.urls', namespace='normativa')),

    url(r'^programacion/', include('programacion.urls', namespace='programacion')),
)
