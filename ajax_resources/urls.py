from django.conf.urls.defaults import *

urlpatterns = patterns('ajax_endpoints.views',
    (r'^(?P<application>\w+)/(?P<resource>\w+).json', 'resource_loader'),
)

