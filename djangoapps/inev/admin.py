from django.contrib import admin 
from djangoapps.inev.models import Question

admin.site.register(Question)#registrar clase en el sistema de admin.
#admin.site.register(Topic)