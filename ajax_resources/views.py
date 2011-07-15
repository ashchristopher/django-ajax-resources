from django.conf import settings
from django.utils.importlib import import_module
from django.utils.translation import ugettext as _
from django.utils import simplejson
from django.http import HttpResponse
from decorator import decorator

from ajax_resources.exceptions import AJAXError, InvalidResourceException


@decorator
def ajax_handler(f, *args, **kwargs):
    try:
        result = f(*args, **kwargs)
    except AJAXError, e:
        result = e.get_response()
    return result


@ajax_handler
def resource_loader(request, application, resource, **kwargs):
    """ 
    Loads and AJAX endpoint resource.
    """
    try:
        module = import_module('%s.ajax_resources' % application)
        resource_func = getattr(module, resource)
    except (ImportError, AttributeError):
        if settings.DEBUG:
            import traceback
            print traceback.print_exc()
        raise AJAXError(404, 'AJAX resource does not exist.')

    data = resource_func(request)

    if not isinstance(data, dict):
        raise InvalidResourceException('Resource did not return a dict.')

    response = HttpResponse(simplejson.dumps(data, indent=4))
    response['Content-Type'] = 'application/json'

    return response


    