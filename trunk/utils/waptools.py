from django.template import loader
from django.http import HttpResponse
	
def render_to_response(*args, **kwargs): 	    
    httpresponse_kwargs = {'mimetype':'text/vnd.wap.wml'}
    return HttpResponse(loader.render_to_string(*args, **kwargs), **httpresponse_kwargs)