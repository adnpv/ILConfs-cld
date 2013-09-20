

from django.http import HttpResponse
from django.shortcuts import render_to_response	
from djangoapps.moderat.models import Quest, Choice
import json


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

