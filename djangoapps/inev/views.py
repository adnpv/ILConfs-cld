

from django.http import HttpResponse
from django.shortcuts import render_to_response
from djangoapps.moderat.models import Quest, Choice
from djangoapps.inev.models import Question
from djangoapps.event.models import Event, Topic
from djangoapps.userp.models import User, Ticket
#import json
from django.utils import simplejson as json2
from django.core import serializers

import requests

#resolv multiple choice
def answer(request):
	response_data = {}
	if request.method == 'GET':
		choice=request.GET['send_resul']
		question_id=request.GET['quest']
		#q = Quest.objects.get(id=question_id)
		n= choice.split('-', 1 );
		chu= n[1]
		print chu
		valcheck = Choice.objects.filter(id=chu)
		if valcheck.count() > 0:
			response_data=almacenar(chu)
		else:
			loadnewdata()
			#ingresar valor
	return HttpResponse(json2.dumps(response_data), mimetype="application/json")

#funcion para las respuestas.
def almacenar(valu):
	response_data = {}
	cho = Choice.objects.get(id=valu)#tambn quest ", quest=q"
	initial_chon = cho.nchoices
	cho.nchoices += 1
	cho.save()
	last_chon = cho.nchoices
	print "DONE"
	if initial_chon != last_chon :
		response_data['result'] = 'Exito'
		response_data['message'] = 'Gracias por Participar'
	else:
		response_data['result'] = 'Error'
		response_data['message'] = 'Su Votacion no se conto'
	return response_data

#funcion actualizar db segun json..... a eliminar!!
def loadnewdata():
	r=requests.get('http://pitreal.hostei.com/eventos/jsonparapublico/pregsalpubl.json')
	data = r.json()
	i=0
	opcion = {}
	for d in data:

		if i == 0:
			pregunta= d["nombre"]
			idpreg= d["idpregunta"]
			#crear pregunta y guardarla
			preg = Quest(name=pregunta, id= idpreg, status=1)
			preg.save()
		else:
			key = str(d["idalternativa"])
			opcion[key]=d["nombre"]



	# return data[0]["nombre"]

def responder_de_web(request): #traer data y hacer push en mobil
	response_data = {}
	data ="nop"
	if request.method == 'GET':

		#r = requests.get('http://elcomercio.pe/html/noticia/0/1/4/5/3/1453463/1453463compacto.json')

		r=requests.get('https://github.com/timeline.json')
		data2 = r.json()
		#data = json2.dumps(data2,sort_keys='nice',indent=4)
	#print data
	return HttpResponse(json2.dumps(data2), mimetype="application/json")

#def servir_de_web(): #traer data y hacer push en mobil
#	"elcomercio.pe/html/noticia/0/1/4/5/3/1453463/1453463compacto.json"


#antiguoooooooooooooooooooo
def get_choices(request):
	response_data = {}
	result = []


	if request.method == 'GET':
		callback = request.GET.get('callback')
		pre=request.GET['query']

		if pre == "all":
			result.append({"user":"exito"})
			result.append({"key":"Gracias por Participar"})
			response_data['result'] = 'Exito'
			response_data['message'] = 'Gracias por Participar'

			print response_data['message']
		else:
			response_data['result'] = 'Error'
			response_data['message'] = 'Su Votacion no se conto'


	jsonString = json2.dumps(result,sort_keys='nice',indent=4)

	return HttpResponse(jsonString, content_type='application/json')

def event(request,event_id=1):
	return render_to_response('event.html',
								{'event':Event.objects.get(id=event_id),})


#traer data de php.
def quest(request):
	que=request.GET.get('que')
	q = Quest.objects.get(id=que)

	#urlriq="http://172.18.7.9/eventos/jsonparapublico/pregsalpubl.json"
	data = [choice.json() for choice in Choice.objects.all().filter(quest=q)]
	#nice = 'nice' in request.GET

	response_data = {}
	if request.method == 'GET':
		r=requests.get('http://pitreal.hostei.com/eventos/jsonparapublico/pregsalpubl.json')
		data2 = r.json()
		#data2 = json2.load(r.json())

	#jsonString = json2.dumps(data,sort_keys=nice,indent=4 if nice else None)
	jsonString = json2.dumps(data2,sort_keys='nice',indent=4)
	# if que:
	# 	jsonString = '%s (%s)' %('?', jsonString)
        #jsonString = '{%s %s}' %('"events":', jsonString)
	return HttpResponse(jsonString, content_type='application/json')










def dausprueba(request):
	response_data = {}
	result = []


	if request.method == 'GET':
		callback = request.GET.get('callback')
		pre=request.GET['query']

		if pre == "all":
			result.append({"user":"exito"})
			result.append({"key":"Gracias por Participar"})
			response_data['result'] = 'Exito'
			response_data['message'] = 'Gracias por Participar'

			print response_data['message']
		else:
			response_data['result'] = 'Error'
			response_data['message'] = 'Su Votacion no se conto'


	jsonString = json2.dumps(result,sort_keys='nice',indent=4)

	return HttpResponse(jsonString, content_type='application/json')




def make_question(request):
	response_data = {}
	if request.method == 'GET':
		titu=request.GET['titulo']
		detall=request.GET['detalle']
		tema_id=request.GET['idtema']
		#user_id=request.GET['idus']
		#crear pregunta y guardarla
		useri = User.objects.get(id=1)	#iduser
		topici = Topic.objects.get(id=1)  #idtopic   era 3
		preg = Question(name=titu, detail= detall)#, iduser=1, idthema= 1)
		#nuevo(3):
		#pregu = preg.save(commit=false)
		preg.topic = topici
		preg.user = useri

						#     if request.method == 'GET':
						#         f = TopicForm(request.POST)
						#         if f.is_valid():
						#             t = f.save(commit=false)#not push yet.
						#             #more values... to event yes.
						#             t.event = e
						#             t.save()


		preg.save()
		response_data['result'] = 'gracias'
		# if initial_chon != last_chon :
		# 	response_data['result'] = 'Exito'
		# 	response_data['message'] = 'Gracias por Participar'
		# else:
		# 	response_data['result'] = 'Error'
		# 	response_data['message'] = 'Su Votacion no se conto'
	return HttpResponse(json2.dumps(response_data), mimetype="application/json")


#obtener manualmente opciones
def manuals(request):
	return render_to_response('manual_gets.html')

def manual_get_quests(request):
	response_data = {}
	datok = 1
	opc1=[]
	new=request.GET.get('new')
	if new == '1':
		if request.method == 'GET':
			r=requests.get('http://pitreal.hostei.com/eventos/jsonparapublico/pregsalpubl.json')
			#datok=r.content
			# data2 = json2.dumps(r.content) #json3.load(r.content)# data2 = r.json()
			#    #dataform = #str(r.content).strip("'<>() ").replace('\'', '\"')
			# data3 = json2.loads(data2)#.decode('utf-8')#str(r.content))
			
			# print r.content

			# print repr(data3)
			# datok= data3

			data2 = r.json()
			data3 =json2.loads(r.content)
			datok= data3[0]['nombre']

			idpreg=data3[0]['idpregunta']
			nombrepreg= data3[0]['nombre']
			#idtema= data3[0]['idtema']
			idtema= 1
			#datok= data2[0]['nombre']
			#datok = len(data2)

			#quest!!!
			topici = Topic.objects.get(id=idtema)  #idthema

			q=Quest(name=nombrepreg,status=1,id=idpreg)
			q.topic = topici
			#multopc = q.save(commit=false)
			#multopc.topic = topici

			#multopc.save()
			q.save()
			#reg = Quest(name=titu, detail= detall)#, iduser=1, idthema= 1)
			for i in range(len(data3)):#antes 2
				if i == 0:
					print 'no'
				else:
					opc1.append(data3[i]['nombre'])#antes2
					idalternativa=data3[i]['idalternativa']
					nombrealtern=data3[i]['nombre']

					cho=Choice(name=nombrealtern,nchoices=0,id=idalternativa)
					cho.quest = q
					cho.save()
			 		#opc1[i]=data2[i]['nombre']

		jsonString = json2.dumps(data3,sort_keys='nice',indent=4)

		#hacer push! notificacion al celular!!!
		#datok = jsonString
	return render_to_response('manual_gets.html', {'pregunta':datok,
													'opc1':opc1,})

def jsonmultipleopc(request):

	if request.method == 'GET':
		idquest=request.GET.get('id')
		questi = Quest.objects.get(id=idquest)
    	data = questi.json() #for quest in Quest.objects.all().order_by('name')]
    	nice = 'nice' in request.GET

    	callback = request.GET.get('callback')

    	jsonString = json2.dumps(data,sort_keys=nice,indent=4 if nice else None)
    	if callback:
        	jsonString = '%s (%s)' %(callback, jsonString)
        #jsonString = '{%s %s}' %('"events":', jsonString)

    	return HttpResponse(jsonString, content_type='application/json')
	return HttpResponse('jsonString', content_type='application/json')

def jsonpreguntos(request):

	if request.method == 'GET':
		idtopicu=request.GET.get('id')
		topicn = Topic.objects.get(id=idtopicu)
		#questi = Question.objects.filter(topic=topicn)
    	data = [questi.json() for questi in Question.objects.filter(topic=topicn)]
    	nice = 'nice' in request.GET

    	callback = request.GET.get('callback')

    	jsonString = json2.dumps(data,sort_keys=nice,indent=4 if nice else None)
    	if callback:
        	jsonString = '%s (%s)' %(callback, jsonString)
        #jsonString = '{%s %s}' %('"events":', jsonString)

    	return HttpResponse(jsonString, content_type='application/json')
	return HttpResponse('jsonString', content_type='application/json')

def manual_get_users():

	return HttpResponse(jsonString, content_type='application/json')

def manual_get_events():

	return HttpResponse(jsonString, content_type='application/json')


def manual_get_topics():

	return HttpResponse(jsonString, content_type='application/json')


# def observus(request):
# 	response_data = {}
# 	if request.method == "OPTIONS":
# 		response = HttpResponse()
# 		response['Access-Control-Allow-Origin'] = '*'
# 		response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
# 		response['Access-Control-Max-Age'] = 1000
# 		# note that '*' is not valid for Access-Control-Allow-Headers
# 		response['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept'
# 		return response

# 	if request.method == 'GET':
# 		resu=request.GET['quesu']

# 		if resu =="all":
# 			response_data['result'] = 'Exito'
# 			response_data['message'] = 'Gracias por Participar'
# 		else:
# 			response_data['result'] = 'Error'
# 			response_data['message'] = 'Su Votacion no se conto'
# 	return HttpResponse(json2.dumps(response_data), mimetype="application/json")

# def add_topic(request, event_id):
#     e = Event.objects.get(id=event_id)

#     if request.method == 'GET':
#         f = TopicForm(request.POST)
#         if f.is_valid():
#             t = f.save(commit=false)#not push yet.
#             #more values... to event yes.
#             t.event = e
#             t.save()
#             return HttpResponseRedirect('/event/get/%s' % event_id)
#     else:
#         f=TopicForm()
#     args ={}
#     args.update(csrf(request))

#     args['article']=a
#     args['form']=f

#     return render_to_response('add_topic.html',args)