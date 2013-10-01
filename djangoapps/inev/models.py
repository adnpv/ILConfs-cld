from django.db import models


# Create your models here.
class Question(models.Model):
	name = models.CharField(max_length=50)
	detail = models.CharField(max_length=50, null=True, blank=True)
	iduser = models.IntegerField()
	idthema = models.IntegerField(default=1)
	def __unicode__(self):
 		return self.name

class User(models.Model):
	iduser = models.IntegerField()
	name = models.CharField(max_length=50) #nombre a colocar en el cel.
	password = models.CharField(max_length=50)

class Ticket(models.Model):
	ticket_num = models.IntegerField()	#identificar , autentificador!!!!
	iduser = models.ForeignKey(User)
	idevent = models.IntegerField()	#no todo dato, solo pedir el id evento y que usuarios estan en el.
	#validar el usuario(id)
     