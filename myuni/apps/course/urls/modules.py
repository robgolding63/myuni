from django.conf.urls.defaults import *

from myuni.apps.course.models import Module
from myuni.apps.course import views

urlpatterns = patterns('',
	
	url(r'^$', views.module_list, {'template_name': 'course/module_list.html'}, name='course_module_list'),
	
	url(r'^all/$', views.module_list, {'queryset': Module.objects.all().select_related(), 'template_name': 'course/module_list_all.html'}, name='course_module_list_all'),
	
	url(r'^(?P<year>[0-9-]+)/(?P<semester>[\w-]+)/(?P<module_code>\w+)/$', views.module_detail, {'template_name': 'course/module_detail.html'}, name='course_module_detail'),
	
)
