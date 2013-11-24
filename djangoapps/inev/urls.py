from django.conf.urls import patterns, include, url
#from event.views import HelloTemplate#agregar el class view! desde nuestras vistas

urlpatterns= patterns('djangoapps.inev.views',
	#url(r'^$','events'),
	url(r'^resolv/$','answer'),
	url(r'^jsonquest/$','quest'),



	
	#url(r'^observa/$','observus'),

	url(r'^obtener/$','dausprueba'),
	url(r'^getquest_cho/$','get_choices'),
	url(r'^comerce/$','responder_de_web'),
	
	url(r'^question/$','make_question'),

	#url(r'^get/(?P<event_id>\d+)/$','event'),
	#url(r'^language/(?P<language>[a-z\-]+)/$','event.views.language'),

	url(r'^getsdata/$','manuals'),
	url(r'^getquest/$','manual_get_quests'),

	url(r'^jsonmquest/$','jsonmultipleopc'),

	url(r'^jsonquestion/$','jsonpreguntos'),
	url(r'^datel/$','datafrommyserver'),
	#url(r'^newmquest/$','insert_quests'),
	url(r'^enviaq/$','enviar_quest_nueva'),
	url(r'^newquest/$','insert_quests'),


	url(r'^allmopc/$','jsonmopc_All'),


	url(r'^jlastq/$','lastquests'),
	url(r'^resolvf/$','answerf'),
)
