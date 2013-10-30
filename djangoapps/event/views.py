from django.http import HttpResponse

#from django.template.loader import get_template #ver carpeta templates
#from django.template import Context #paso datos(grupos)
	#se envio en el contexto, {{}} se pasara y render estos.

from django.shortcuts import render_to_response	
#clase!!
#from django.views.generic.base import TemplateView # sabe como mostrar un template.


from djangoapps.event.models import Event, Topic
from forms import EventForm, TopicForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone

from django.core import serializers
import json

def events(request):
	return render_to_response('events.html',
								{'events':Event.objects.all(),})#agregar valor.
	#render_to_response(template,variables de contexto)
def event(request,event_id=1):
	return render_to_response('event.html',
								{'event':Event.objects.get(id=event_id),})

def add_topic(request, event_id):
    e = Event.objects.get(id=event_id)

    if request.method == 'POST':
        f = TopicForm(request.POST)
        if f.is_valid():
            t = f.save(commit=false)#not push yet.
            #more values... to event yes.
            t.event = e
            t.save()
            return HttpResponseRedirect('/event/get/%s' % event_id)
    else:
        f=TopicForm()
    args ={}
    args.update(csrf(request))

    args['article']=a
    args['form']=f

    return render_to_response('add_topic.html',args)
def jsonevent(request):
    data = [event.json() for event in Event.objects.all().order_by('name')]
    jsonString = json.dumps(data,indent=4)#sort_keys='nice'

    #nice = 'nice' in request.GET
    #callback = request.GET.get('callback')

    #jsonString = json.dumps(data,sort_keys=nice,indent=4 if nice else None)
    #if callback:
    #    jsonString = '%s (%s)' %(callback, jsonString)
    #    #jsonString = '{%s %s}' %('"events":', jsonString)
    return HttpResponse(jsonString, content_type='application/json')
    #http://localhost:8000/json/jsonev/?nice
    #return HttpResponse(json.dumps(data), content_type='application/json')

def jsonevent2(request):
    data = serializers.serialize("json", Event.objects.all().order_by('name'))
    return HttpResponse(data, mimetype='application/json')


def insert_events(request):
    response_data = {}

#     if request.method == 'GET':
#         username=request.GET.get('username')
#         password=request.GET.get('password')
#         print username,password
#     #   #r=requests.get('http://pitreal.hostei.com/eventos/jsonparapublico/pregsalpubl.json')
#         payload ={'user': username,'password':password }
        
#     #   r=requests.post('http://pitreal.hostei.com/eventos/', data = payload)#,'usernami' = username)
#         r=requests.get('http://localhost:8000/user/petic/', params = payload)#,'usernami' = username)

#         #data2 = r.json()
#         data3 =json2.loads(r.content)

#         nombre= data3['nombre']# [{'datok'}] (son arreglos y se antepone un [0])
#         userid = data3['userid']
#         apellido = data3['apellido']
#         #crear usuario segun data obtenida!!!!!!!!!!!!!!!!!
#         #nuevou = User(id=userid,name=nombre,lastname=apellido)

#         #validar asignacion solo si existe
#         usuario = User.objects.get(id=userid)

#         eventos = data3['events']
#         #print repr(eventos[1])
#         for i in range(len(eventos)):#antes 2
#             idevento = eventos[i]['idevent']
#             evento = Event.objects.get(id=idevento)

#             codigoauth = eventos[i]['codauth']
#             #print type(codigoauth) 
#             ticket = Ticket(user=usuario,event=evento,ticket_num=codigoauth)
#             #ticket.save() #guardar tickets pero no aun!!, tambien cargar esto cada vez q ingrese denuevo a la app!! OJO

#         response_data['nombre']= nombre
#         response_data['apellido']= apellido
#         response_data['userid']= userid
    jsonString = json2.dumps(response_data,indent=4)

#     #hacer push! notificacion al celular!!!
#     #datok = jsonString
    return HttpResponse(jsonString, content_type="application/json; charset=utf-8")
