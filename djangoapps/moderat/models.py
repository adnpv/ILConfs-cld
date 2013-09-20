from django.db import models

from djangoapps.event.models import Topic

class Quest(models.Model):
	topic = models.ForeignKey(Topic)
	name = models.CharField(max_length=500)
	status = models.IntegerField()
	#status = models.CharField(max_length=15)
	description = models.TextField()
	start_hour = models.TimeField('Hora de Inicio')
	end_hour = models.TimeField('Hora de Fin')
	room = models.CharField(max_length=300)
	likes = models.IntegerField()

	def __unicode__(self):
		return self.name

class Choice(models.Model):
	name = models.CharField(max_length=100)
	#nchoice = models.IntegerField() el id se provee al enviar la data!!, para colocarla en dif. opciones, seguridad?
	nchoices = models.IntegerField()
	quest = models.ForeignKey(Quest)

	def __unicode__(self):
		return self.name
	