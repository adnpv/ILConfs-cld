

from django.http import HttpResponse
from django.shortcuts import render_to_response	
from djangoapps.moderat.models import Quest, Choice
#import json
from django.utils import simplejson as json
from django.core import serializers

 
def answer(request):
	response_data = {}
	if request.method == 'POST':
		choice=request.POST['send_resul']
		question_id=request.POST['quest']
		q = Quest.objects.get(id=question_id)

		cho = Choice.objects.get(id=choice)#tambn quest ", quest=q"
		cho.nchoices += 1
		if cho.save():
			response_data['result'] = 'Exito'
			response_data['message'] = 'Gracias por Participar'
		else:
			response_data['result'] = 'Error'
			response_data['message'] = 'Su Votacion no se conto'
	return HttpResponse(json.dumps(response_data), mimetype="application/json")

def event(request,event_id=1):
	return render_to_response('event.html',
								{'event':Event.objects.get(id=event_id),})

def quest(request, quest_id=1):
	que=request.GET.get('que')
	q = Quest.objects.get(id=que)
	data = [choice.json() for choice in Choice.objects.all().filter(quest=q)]
	nice = 'nice' in request.GET

	jsonString = json.dumps(data,sort_keys=nice,indent=4 if nice else None)
	if que:
		jsonString = '%s (%s)' %('?', jsonString)
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
	

	jsonString = json.dumps(result,sort_keys='nice',indent=4)

	return HttpResponse(jsonString, content_type='application/json')

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