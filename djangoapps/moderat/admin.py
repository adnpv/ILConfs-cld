from django.contrib import admin 
from djangoapps.moderat.models import Quest, Choice
	#nuestra app.

admin.site.register(Quest)#registrar clase en el sistema de admin.
admin.site.register(Choice)