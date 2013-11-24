from django.db import models

from djangoapps.event.models import Topic, Event

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
	nchoices = models.IntegerField(default=0)
	quest = models.ForeignKey(Quest)
	def json(self):
		fields =('id','nchoices',)
		return dict((field, self.__dict__[field])for field in fields) #armando dict, basado en los campos
			#attrib, value
	def jsonfetch(self):
		return {
			'idalternativa':self.id,
			'nombre':self.name,
		}
	def __unicode__(self):
		return self.name


class Lastquest(models.Model):
	#event = models.ForeignKey(Event) #!!!!!!!!!!!!!!!!!!!!!!!!!!
	name = models.CharField(max_length=500)
	#status = models.IntegerField()
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
	def jsonfetch(self):
		return{
			'idalternativa':self.id,
			'nombre':self.name,
		}
	def json(self):
		fields =('id','nchoices',)
		return dict((field, self.__dict__[field])for field in fields) #armando dict, basado en los campos
			#attrib, value
	def __unicode__(self):
		return self.name
	
class FlqSolv(models.Model):		#n(preguntas) por evento!!!! 19! por evento!
	event = models.ForeignKey(Event)
	lcho = models.ForeignKey(LastChoice)
	lque = models.ForeignKey(Lastquest)
	nchoices = models.IntegerField()
	
	def __unicode__(self):
		return "%s,-- %s, OPC: %s"%(self.event.name, self.lque.id, self.lcho.name)