from django import forms
from models import Event, Topic

class EventForm(forms.ModelForm):
    class Meta:
		model = Event
		fields= ('name','description','start_date','end_date','location','status')

class TopicForm(forms.ModelForm):
    class Meta:
		model = Topic
		fields= ('name','description','start_hour','end_hour','room')    