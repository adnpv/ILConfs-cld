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
			'choices':[choice.json() for choice in Choice.objects.filter(quest=self)]
		}

	def __unicode__(self):
		return self.name

class Choice(models.Model):
	name = models.CharField(max_length=200)
	#nchoice = models.IntegerField() el id se provee al enviar la data!!, para colocarla en dif. opciones, seguridad?
	nchoices = models.IntegerField()
	quest = models.ForeignKey(Quest)
	def json(self):
		fields =('id','nchoices',)
		return dict((field, self.__dict__[field])for field in fields) #armando dict, basado en los campos
			#attrib, value
	def __unicode__(self):
		return self.name


class Lastquest(models.Model):
	name = models.CharField(max_length=500)
	status = models.IntegerField()
	#status = models.CharField(max_length=15)
	def json(self):
		return {
			'questid':self.id,
			'choices':[lchoice.json() for lchoice in Lastchoice.objects.filter(lquest=self)]
		}

	def __unicode__(self):
		return self.name

class LastChoice(models.Model):
	name = models.CharField(max_length=200)
	#nchoice = models.IntegerField() el id se provee al enviar la data!!, para colocarla en dif. opciones, seguridad?
	nchoices = models.IntegerField()
	lquest = models.ForeignKey(Lastquest)
	def json(self):
		fields =('id','nchoices',)
		return dict((field, self.__dict__[field])for field in fields) #armando dict, basado en los campos
			#attrib, value
	def __unicode__(self):
		return self.name
	