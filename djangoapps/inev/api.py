from tastypie.resources import ModelResource
from djangoapps.inev.models import Question


class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'