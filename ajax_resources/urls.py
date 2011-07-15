from django.conf.urls.defaults import *

urlpatterns = patterns('ajax_resources.views',
    (r'^(?P<application>\w+)/(?P<resource>\w+).json', 'resource_loader'),
)

