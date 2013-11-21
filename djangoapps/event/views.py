from django.http import HttpResponse
from ast import literal_eval as lit
#from django.template.loader import get_template #ver carpeta templates
#from django.template import Context #paso datos(grupos)
	#se envio en el contexto, {{}} se pasara y render estos.

from django.shortcuts import render_to_response	
#clase!!
#from django.views.generic.base import TemplateView # sabe como mostrar un template.


from djangoapps.event.models import Event, Topic, Speaker
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
    print request.GET.urlencode
    print "simple get:"
    print request.GET
    if request.method == 'GET':

        #data3 =json2.loads(request)

        mydict = dict(request.GET.iterlists())
        # print mydict
        # print "dataaaaaa"
        for keys,values in mydict.items():
            data3 = lit(keys)[0]
        
        print data3['nombre']
        # #print data3['idevento']


        idevento = data3['idevento']
        nombre= data3['nombre']# [{'datok'}] (son arreglos y se antepone un [0])
        start_date = data3['fechainicio']
        #arrinicio = start_date.split('-',3)

        end_date = data3['fechafin']
        start_hour = data3['horainicio']
        end_hour = data3['horafin']

        #??????descripcion = request.GET.get('descripcion')#?????????????
        #start_date = data3['start_date']    #pasar año, mes y dia (armarlo aca)
        #end_date = data3['end_date']
        lugar = data3['lugar']
        latitud = data3['latitud']
        longitud = data3['longitud']

        #destacado = data3['destacado']
        #estado = data3['estado']

        #organizador = data3['organizador')# idusuari]
        #likes = data3['likes']

        descripcion ="evento traido"
        estado=0
        likes=1
        organizador ="SHO"

        #crear usuario segun data obtenida!!!!!!!!!!!!!!!!!
        eventu = Event(id=idevento, name = nombre,
                        description = descripcion,
                        start_date = start_date,end_date = end_date, 
                        start_hour = start_hour,end_hour = end_hour, 
                        location = lugar,latitude = latitud, 
                        longitude = longitud, status = estado,
                        likes = likes, organizer = organizador)
        eventu.save()
        if eventu.id != 0 :
            response_data['resultado']= "ok"
        else:
            response_data['resultado']= "no"
        
    jsonString = json.dumps(response_data,indent=4)

#     #hacer push! notificacion al celular!!!
#     #datok = jsonString
    return HttpResponse(jsonString, content_type="application/json; charset=utf-8")

def insert_topics(request):
    response_data = {}
    print request.GET.urlencode
    print "simple get:"
    print request.GET

    if request.method == 'GET':
        #data3 =json2.loads(request)

        mydict = dict(request.GET.iterlists())
        # print mydict
        # print "dataaaaaa"
        for keys,values in mydict.items():
            data3 = lit(keys)[0]

        print data3['nombre']

        idevento = data3['idevento']
        idtema = data3['idtema']
        nombre= data3['nombre']     # [{'datok'}] (son arreglos y se antepone un [0]]
        description = 'temaa'       #data3['descripcion']
        start_hour = data3['horainicio']
        end_hour = data3['horafin']


        #expositorid = data3['idexpositor']
        expositorid = 1
        if isinstance( expositorid, int ):
            speak=Speaker.objects.get(id=expositorid)#ya deberia de existir.
        else:
            speak=Speaker.objects.get(id=1)#guardar un NO definido!!!


        #start_hour = data3['start_hour'] #hora min (armarlo aca)
        #end_hour = data3['end_hour']

        room = "no definida"    #data3['sala']
        likes = 3   #data3['likes']
        status = 0
        eventu = Event.objects.get(id=idevento)
        #crear usuario segun data obtenida!!!!!!!!!!!!!!!!!
        topict = Topic(id=idtema, event= eventu,name = nombre,
                        description = description,
                        start_hour = start_hour,end_hour = end_hour, 
                        room = room, likes = likes, status = status,
                        speaker= speak)
        topict.save()

        if topict.id != 0 :
            response_data['detalle'] = topict.jsondetalle()
            response_data['resultado']= "ok"
        else :
            response_data['resultado']= "no"
        
    jsonString = json.dumps(response_data,indent=4)

#     #hacer push! notificacion al celular!!!
#     #datok = jsonString
    return HttpResponse(jsonString, content_type="application/json; charset=utf-8")



def insert_speaker(request):
    response_data = {}

    if request.method == 'GET':

        mydict = dict(request.GET.iterlists())
        for keys,values in mydict.items():
            data3 = lit(keys)[0]

        idspeak = data3['idexpositor']
        name = data3['nombre']
        lname= data3['apellido']     # [{'datok'}] (son arreglos y se antepone un [0]]
        description = ['descrip']       #data3['descripcion']
        
        speak=Speaker.objects.filter(id=expositor)#ya deberia de existir.
        if speak.count() > 0:
            print "expositor existe"
        else:
            sp = Speaker(id=idspeak,name=name,lastname=lname,description=description)        
            sp.save()

        if sp.id != 0 :
            response_data['resultado']= "ok"
        else:
            response_data['resultado']= "no"
        
    jsonString = json.dumps(response_data,indent=4)
    return HttpResponse(jsonString, content_type="application/json; charset=utf-8")



def detalle_event(request):
    eventos = {}
    data = []
    if request.method == 'GET':
        evid=int(request.GET.get('idevento'))
        evento = Event.objects.get(id=evid)
        data = evento.jsondetalle()

    jsonString = json.dumps(data,indent=4)
    return HttpResponse(jsonString, content_type='application/json')


def temas_evento(request):
    eventos = {}
    data = []
    if request.method == 'GET':
        evid=int(request.GET.get('idevento'))
        evento = Event.objects.get(id=evid)
        for tema in Topic.objects.filter(event=evento):
            data.append(tema.json())

    jsonString = json.dumps(data,indent=4)
    return HttpResponse(jsonString, content_type='application/json')

def detalle_topic(request):
    eventos = {}
    data = []
    if request.method == 'GET':
        toid=int(request.GET.get('idtopic'))
        print "TOPICOOOOO"
        print toid
        tema = Topic.objects.get(id=toid)
        data = tema.jsondetalle()

    jsonString = json.dumps(data,indent=4)
    return HttpResponse(jsonString, content_type='application/json')

def spek_tema(request):
    data = []
    if request.method == 'GET':
        topico=request.GET.get('top')
        topicu = Topic.objects.get(id=topico)

        # idexpositor = topicu.speaker.id

        # spek = Speaker.objects.get(id=idexpositor)
        data = topicu.jsonexpo()
        
        jsonString = json.dumps(data,indent=4)
        print jsonString
        # return HttpResponse(jsonString, content_type="text/html; charset=utf-8")#content_type='application/json', charset=utf-8)
    return HttpResponse(jsonString, content_type='application/json')

