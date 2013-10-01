

from django.http import HttpResponse
from django.shortcuts import render_to_response	
from djangoapps.moderat.models import Quest, Choice
from djangoapps.inev.models import Question
#import json
from django.utils import simplejson as json2
from django.core import serializers

import requests
def answer(request):
	response_data = {}
	if request.method == 'GET':
		choice=request.GET['send_resul']
		question_id=request.GET['quest']
		#q = Quest.objects.get(id=question_id)
		n= choice.split('-', 1 );
		chu= n[1]
		print chu
		cho = Choice.objects.get(id=chu)#tambn quest ", quest=q"
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
	return HttpResponse(json2.dumps(response_data), mimetype="application/json")

 
def responder_de_web(request): #traer data y hacer push en mobil
	response_data = {}
	data ="nop"
	if request.method == 'GET':

		#r = requests.get('http://elcomercio.pe/html/noticia/0/1/4/5/3/1453463/1453463compacto.json')

		r=request.get('https://github.com/timeline.json')
		data2 = r.json()
		#data = json2.dumps(data2,sort_keys='nice',indent=4)
	#print data
	return HttpResponse(json2.dumps(data2), mimetype="application/json")

def servir_de_web(): #traer data y hacer push en mobil
	"elcomercio.pe/html/noticia/0/1/4/5/3/1453463/1453463compacto.json"
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

def quest(request, quest_id=1):
	que=request.GET.get('que')
	q = Quest.objects.get(id=que)
	#urlriq="http://172.18.7.9/eventos/jsonparapublico/pregsalpubl.json"
	data = [choice.json() for choice in Choice.objects.all().filter(quest=q)]
	nice = 'nice' in request.GET

	jsonString = json2.dumps(data,sort_keys=nice,indent=4 if nice else None)
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
		preg = Question(name=titu, detail= detall, iduser=1, idthema= 1)
		preg.save()
		response_data['result'] = 'gracias'
		# if initial_chon != last_chon :
		# 	response_data['result'] = 'Exito'
		# 	response_data['message'] = 'Gracias por Participar'
		# else:
		# 	response_data['result'] = 'Error'
		# 	response_data['message'] = 'Su Votacion no se conto'
	return HttpResponse(json2.dumps(response_data), mimetype="application/json")


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