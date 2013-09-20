from django.contrib import admin 
from djangoapps.event.models import *
	#nuestra app.

admin.site.register(Event)#registrar clase en el sistema de admin.
admin.site.register(Topic)