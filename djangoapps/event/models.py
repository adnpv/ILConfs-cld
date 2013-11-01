from django.db import models
from datetime import datetime   
# Create your models here.
class Event(models.Model):
	#idevent = models.IntegerField()
	name = models.CharField(max_length=200)
	description = models.TextField()
	start_date = models.DateField('initial date',default=datetime.now, blank=True)
	end_date = models.DateField('end date',default=datetime.now, blank=True)
	location = models.CharField(max_length=300)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	status = models.IntegerField()
	#status = models.CharField(max_length=15)
	likes = models.IntegerField()	#destacado
	organizer = models.CharField(max_length=50)


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
			#'inicio':self.start_date,
			'lugar':self.location,
			'org':self.organizer,
		}

	'''class Meta:
		verbose_name = _('Event')
		verbose_name_plural = _('Events')'''

	def __unicode__(self):
		#para identificar en las partes de definiciones el nombre
		return self.name

class Topic(models.Model):
	#idtopic = models.IntegerField()
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=200)
	description = models.TextField()
	start_hour = models.TimeField('Hora de Inicio')#modificar a default = ahora
	end_hour = models.TimeField('Hora de Fin')#modificar a default = ahora
	room = models.CharField(max_length=300)
	likes = models.IntegerField()

	def json(self):
		return {
			'idev': self.id,
			'name':self.name,
		}

	def jsondetalle(self):
		return {
			'idtem': self.id,
			'name':self.name,
			'desc':self.description,
			#'h_inicio':self.start_hour,
			'room':self.room,
		}	

	def __unicode__(self):
		return self.name