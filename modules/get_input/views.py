from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('get_input/index.html')
    context = {
        'message': "Hello world!",
    }
    return HttpResponse(template.render(context, request))

def response(request):
    template = loader.get_template('get_input/response.html')
    context = {
        'name'       : request.POST['name'],
        'start_year' : request.POST['start_year'],
        'end_year'   : request.POST['end_year'],
    }
    return HttpResponse(template.render(context, request))


