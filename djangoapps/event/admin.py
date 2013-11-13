from django.contrib import admin 
from djangoapps.event.models import Event, Topic, Speaker
	#nuestra app.

admin.site.register(Event)#registrar clase en el sistema de admin.
admin.site.register(Speaker)
admin.site.register(Topic)