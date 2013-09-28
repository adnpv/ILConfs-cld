from django.conf.urls import patterns, include, url
#from event.views import HelloTemplate#agregar el class view! desde nuestras vistas
urlpatterns= patterns('djangoapps.inev.views',
	#url(r'^$','events'),
	url(r'^resolv/$','answer'),
	url(r'^jsonquest/$','quest'),


	
	#url(r'^observa/$','observus'),

	url(r'^obtener/$','dausprueba'),

	#url(r'^get/(?P<event_id>\d+)/$','event'),
	#url(r'^language/(?P<language>[a-z\-]+)/$','event.views.language'),
)
