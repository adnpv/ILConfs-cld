from django.contrib import admin 
from djangoapps.userp.models import User, Ticket
	#nuestra app.

admin.site.register(User)#registrar clase en el sistema de admin.
admin.site.register(Ticket)