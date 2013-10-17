from django.db import models
from djangoapps.event.models import Topic
from djangoapps.userp.models import User
 

# Create your models here.
class Question(models.Model):#preguntas a expositor
	name = models.CharField(max_length=50)
	detail = models.CharField(max_length=50, null=True, blank=True)
	#iduser = models.IntegerField()
	#idtopic = models.IntegerField(default=1)
	user = models.ForeignKey(User)
	topic = models.ForeignKey(Topic)
	def json(self):
		return {
			'idpreg':self.id,
			'nombre':self.name,
			'detalle':self.detail,
			'usuarioid':self.user.id #,
			#'temaid':self.topic.id
		}
	def __unicode__(self):
 		return self.name

