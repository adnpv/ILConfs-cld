# Create your views here.
import django
import django.middleware.csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from djangoapps.moderat.models import Quest, Choice
from djangoapps.inev.models import Question
from djangoapps.event.models import Event, Topic
from djangoapps.userp.models import User, Ticket
from django.core.context_processors import csrf
#import json
from django.utils import simplejson as json2
from django.core import serializers

import requests
# -*- coding: utf-8 -*-
#resolv multiple choice
def login2(request):
	response_data = {}
	if request.method == 'POST':
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

#@method_decorator(ensure_csrf_cookie)
def login(request):
	response_data = {}

	if request.method == 'GET':
		username=request.GET.get('username')
		password=request.GET.get('password')
		print username,password
	# 	#r=requests.get('http://pitreal.hostei.com/eventos/jsonparapublico/pregsalpubl.json')
		payload ={'user': username,'password':password }
		
	#	r=requests.post('http://pitreal.hostei.com/eventos/', data = payload)#,'usernami' = username)
		r=requests.get('http://localhost:8000/user/petic/', params = payload)#,'usernami' = username)

		#data2 = r.json()
	 	data3 =json2.loads(r.content)

		nombre= data3['nombre']# [{'datok'}] (son arreglos y se antepone un [0])
		userid = data3['userid']
		apellido = data3['apellido']
		#crear usuario segun data obtenida!!!!!!!!!!!!!!!!!
		#nuevou = User(id=userid,name=nombre,lastname=apellido)

		#validar asignacion solo si existe
		usuario = User.objects.get(id=userid)

		eventos = data3['events']
		#print repr(eventos[1])
		for i in range(len(eventos)):#antes 2
			idevento = eventos[i]['idevent']
			evento = Event.objects.get(id=idevento)

			codigoauth = eventos[i]['codauth']
			#print type(codigoauth)	
			ticket = Ticket(user=usuario,event=evento,ticket_num=codigoauth)
			#ticket.save() #guardar tickets pero no aun!!, tambien cargar esto cada vez q ingrese denuevo a la app!! OJO

		response_data['nombre']= nombre
		response_data['apellido']= apellido
		response_data['userid']= userid
	jsonString = json2.dumps(response_data,indent=4)

	#hacer push! notificacion al celular!!!
	#datok = jsonString
	return HttpResponse(jsonString, content_type="application/json; charset=utf-8")


#local, ya se tiene la parte de evento asignado y su codigo
	#demo de realizacion de php:
def peticion(request):
	eventos = {}
	if request.method == 'GET':
		userlog=str(request.GET.get('user'))
		#OJO!!!!! FALTA VALIDACION
		usuario = User.objects.get(name=userlog)#ojo username y name es diferente(obiar para simular)
		eventos['userid']=usuario.id
		eventos['nombre']=usuario.name
		eventos['apellido']=usuario.lastname
    	data = [entrada.json() for entrada in Ticket.objects.filter(user=usuario)]
    	print "datoko"
    	eventos['events']= data
    	print eventos
    	#codificar la data
    	jsonString = json2.dumps(eventos,ensure_ascii=False, encoding="utf-8",indent=4)

    	return HttpResponse(jsonString, content_type="application/json; charset=utf-8")

def previo_login(request):
	response_data = {}
	if request.method == 'GET':
		idto=request.GET.get('id')
		if idto == "tokeniko":
			print "hellokoooooooooooooo"
			token = django.middleware.csrf.get_token(request)
			print token
			response_data['result'] = token
			#resp = [response_data]
			# if initial_chon != last_chon :
			# 	response_data['result'] = 'Exito'
			# 	response_data['message'] = 'Gracias por Participar'
			# else:
			# 	response_data['result'] = 'Error'
			# 	response_data['message'] = 'Su Votacion no se conto'
	return HttpResponse(json2.dumps(response_data), mimetype="application/json")

def eventos_user(request):
	eventos = {}
	data = []
	if request.method == 'GET':
		userid=str(request.GET.get('userid'))
		usuario = User.objects.get(id=userid)
		for ticke in Ticket.objects.filter(user=usuario):
			event = ticke.event
			data.append(event.json())

	jsonString = json2.dumps(data,indent=4)
	return HttpResponse(jsonString, content_type='application/json')


