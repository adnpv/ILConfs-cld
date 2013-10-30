from django.db import models

from djangoapps.event.models import Event

class User(models.Model):
	#iduser = models.IntegerField(default=1)
	name = models.CharField(max_length=50) #nombre a colocar en el cel.
	#password = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	suscrib = models.BooleanField()
	def __unicode__(self):
 		return self.name

class Ticket(models.Model):
	ticket_num = models.IntegerField()	#identificar , autentificador!!!!
	user = models.ForeignKey(User)
	event = models.ForeignKey(Event)
	#idevent = models.IntegerField()	#no todo dato, solo pedir el id evento y que usuarios estan en el.
	#validar el usuario(id)
	def json(self):
		return {
			'idevent':self.event.id,
			'codauth':self.ticket_num
		}
	def __unicode__(self):
		tname = "Usuario: "+self.user.name + ", Evento:"+ self.event.name
 		return tname
	    
# Create your models here.
