# Create your views here.
from django.http import HttpResponse

#from django.template.loader import get_template #ver carpeta templates
#from django.template import Context #paso datos(grupos)
	#se envio en el contexto, {{}} se pasara y render estos.

from django.shortcuts import render_to_response	
#clase!!
#from django.views.generic.base import TemplateView # sabe como mostrar un template.


from djangoapps.event.models import Event, Topic
from django.shortcuts import redirect

def home(request):
	return render_to_response('home.html',
								{'events':Event.objects.all(),})#Filtrar los eventos destacados!!
def crear_cuenta(request):

	return redirect('/home/uhome')


def uhome(request):
	return render_to_response('local.html',
								{'events':Event.objects.all(),})#logica para el funcionamiento, ingreso y obtencion de datos
# def event(request,event_id=1):
# 	return render_to_response('event.html',
# 								{'event':Event.objects.get(id=event_id),})


def crear_evento(request):
	return render_to_response('crear_ev.html',
								{'events':Event.objects.all(),})#logica para el funcionamiento, ingreso y obtencion de datos


def contact(request):
	return render_to_response('contact.html',
								{'events':Event.objects.all(),})#logica para el funcionamiento, ingreso y obtencion de datos

def interacc(request,event_id=1):
	return render_to_response('Interactiv_module.html',
								{'event':Event.objects.get(id=event_id),})#logica para el funcionamiento, ingreso y obtencion de datos



def mis_eventos(request):
	return render_to_response('mis_eventos.html',
								{'events':Event.objects.all(),})#logica para el funcionamiento, ingreso y obtencion de datos


def servicio(request):
	return render_to_response('servicio.html',
								{'events':Event.objects.all(),})#logica para el funcionamiento, ingreso y obtencion de datos





def comprar(request):
	return render_to_response('compra_entradas.html',
								{'events':Event.objects.all(),})#logica para el funcionamiento, ingreso y obtencion de datos
def mis_entradas(request):
	return render_to_response('mis_entradas.html',
								{'events':Event.objects.all(),})#logica para el funcionamiento, ingreso y obtencion de datos
def login(request):
	return render_to_response('local.html',
								{'events':Event.objects.all(),})#logica para el funcionamiento, ingreso y obtencion de datos

def events(request):
	return render_to_response('events.html',
								{'events':Event.objects.all(),})#agregar valor.
	#render_to_response(template,variables de contexto)
def event(request,event_id=1):
	return render_to_response('event.html',
								{'event':Event.objects.get(id=event_id),})

