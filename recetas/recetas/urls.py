from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^$','app.views.inicio'),
    url(r'^usuarios/$','app.views.usuarios'),
    url(r'^recetas/$','app.views.lista_recetas'),
    url(r'^receta/(?P<id_receta>\d+)$', 'app.views.detalle_receta'),
    url(r'^sobre/$','app.views.sobre'),
 	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    				{'document_root':settings.MEDIA_ROOT,}
    	),
)
