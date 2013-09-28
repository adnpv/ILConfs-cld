#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from djangoapps.inev.api import QuestionResource

question_resource = QuestionResource()


urlpatterns = patterns('',
	(r'^', include('djangoapps.event.urls')),
	(r'^/$', include('djangoapps.event.urls')),
	(r'^events/$', include('djangoapps.event.urls')),
    (r'^home/', include('djangoapps.cms.urls')),
    (r'^json/', include('djangoapps.event.urls')),
    (r'^adm/', include('djangoapps.admn.urls')),
    (r'^moder/', include('djangoapps.moderat.urls')),
    (r'^interactiv/', include('djangoapps.inev.urls')),
    (r'^api/', include(question_resource.urls)),
    # Examples:
    # url(r'^$', 'ILConfs.views.home', name='home'),
    # url(r'^ILConfs/', include('ILConfs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^secret/admin/', include(admin.site.urls)),
)
