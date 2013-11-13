from django.db import models
from datetime import datetime   
# Create your models here.
class Event(models.Model):
	#idevent = models.IntegerField()
	name = models.CharField(max_length=200)
	description = models.TextField()
	organizer = models.CharField(max_length=50)
	start_date = models.DateField('initial date',default=datetime.now, blank=True)
	end_date = models.DateField('end date',default=datetime.now, blank=True)
	start_hour = models.TimeField('Hora de Inicio', default=datetime.now().time)
	end_hour = models.TimeField('Hora de Fin',default=datetime.now().time)

	location = models.CharField(max_length=300)
	latitude = models.DecimalField(max_digits=15, decimal_places=8)
	longitude = models.DecimalField(max_digits=15, decimal_places=8)
	status = models.IntegerField()
	#status = models.CharField(max_length=15)
	likes = models.IntegerField()	#destacado




	def json(self):
		descri = (self.description).split(' ')[0:20]
		descro = ' '.join(descri)#str(x) for x in list_of_ints
		return {
			'idev': self.id,
			'name':self.name,
			'desc': descro,
		}
	def jsondetalle(self):
		return {
			'idev': self.id,
			'name':self.name,
			'desc':self.description,
			'inicio':str(self.start_date),
			'lugar':self.location,
			'org':self.organizer,
		}

	'''class Meta:
		verbose_name = _('Event')
		verbose_name_plural = _('Events')'''

	def __unicode__(self):
		#para identificar en las partes de definiciones el nombre
		return self.name

class Speaker(models.Model):
	name = models.CharField(max_length=50) 
	lastname = models.CharField(max_length=50)
	description = models.TextField()
	
	def json(self):
		return {
			'idesp': self.id,
			'name': self.name,
			'lname':self.lastname,
			'desc': self.description,
		}


	def __unicode__(self):
		return self.name
		
class Topic(models.Model):
	#idtopic = models.IntegerField()
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=200)
	description = models.TextField()
	start_hour = models.TimeField('Hora de Inicio', default=datetime.now().time)#modificar a default = ahora
	end_hour = models.TimeField('Hora de Fin',default=datetime.now().time)#modificar a default = ahora
	room = models.CharField(max_length=300)
	likes = models.IntegerField()
	status = models.IntegerField() #no iniciado, iniciado, finalizado, ronda preg.
	speaker = models.ForeignKey(Speaker)

	def json(self):
		return {
			'idev': self.event.id,
			'idtem': self.id,
			'name':self.name,
		}

	def jsondetalle(self):
		return {
			'idev':self.event.id,
			'idtem': self.id,
			'name':self.name,
			'desc':self.description,
			'h_inicio':str(self.start_hour),
			'room':self.room,
		}	

	def __unicode__(self):
		return self.name


