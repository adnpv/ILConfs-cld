from django.db import models
from datetime import datetime   
# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	start_date = models.DateField('initial date',default=datetime.now, blank=True)
	end_date = models.DateField('end date',default=datetime.now, blank=True)
	location = models.CharField(max_length=300)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	status = models.IntegerField()
	#status = models.CharField(max_length=15)
	likes = models.IntegerField()


	def json(self):
		return {
			'name':self.name
		}

	'''class Meta:
		verbose_name = _('Event')
		verbose_name_plural = _('Events')'''

	def __unicode__(self):
		#para identificar en las partes de definiciones el nombre
		return self.name

class Topic(models.Model):
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=200)
	description = models.TextField()
	start_hour = models.TimeField('Hora de Inicio')
	end_hour = models.TimeField('Hora de Fin')
	room = models.CharField(max_length=300)
	likes = models.IntegerField()

	def __unicode__(self):
		return self.name