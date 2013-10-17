from django.db import models

from djangoapps.event.models import Topic

class Quest(models.Model):
	topic = models.ForeignKey(Topic)
	name = models.CharField(max_length=500)
	status = models.IntegerField()
	#status = models.CharField(max_length=15)
	def json(self):
		return {
			'topicid':self.topic.id,
			'questid':self.id,
			'name':self.name,
			'choices':[choice.json() for choice in Choice.objects.filter(quest=self)]
		}

	def __unicode__(self):
		return self.name

class Choice(models.Model):
	name = models.CharField(max_length=100)
	#nchoice = models.IntegerField() el id se provee al enviar la data!!, para colocarla en dif. opciones, seguridad?
	nchoices = models.IntegerField()
	quest = models.ForeignKey(Quest)
	def json(self):
		fields =('name','id','nchoices',)
		return dict((field, self.__dict__[field])for field in fields) #armando dict, basado en los campos
			#attrib, value
	def __unicode__(self):
		return self.name
	