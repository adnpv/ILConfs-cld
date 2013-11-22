from django.contrib import admin 
from djangoapps.moderat.models import Quest, Choice ,Lastquest, LastChoice, FlqSolv
	#nuestra app.

admin.site.register(Quest)#registrar clase en el sistema de admin.
admin.site.register(Choice)
admin.site.register(Lastquest)
admin.site.register(LastChoice)
admin.site.register(FlqSolv)
