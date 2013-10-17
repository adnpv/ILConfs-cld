from tastypie.resources import ModelResource
from djangoapps.moderat.models import Quest, Choice
from tastypie import fields


class QuestResource(ModelResource):
    class Meta:
        queryset = Quest.objects.all()
        resource_name = 'quest'

class ChoiceResource(ModelResource):
    quest = fields.ForeignKey(QuestResource, 'quest')
    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choices'