from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from construct_urls import build_esearch_url_year_range

# Create your views here.
def index(request):
    template = loader.get_template('get_input/index.html')
    context = {
        'message': "Hello world!",
    }
    return HttpResponse(template.render(context, request))

def response(request):
    
    template = loader.get_template('get_input/response.html')
    
    name       =     request.POST[ 'name'       ]
    start_year = int(request.POST[ 'start_year' ])
    end_year   = int(request.POST[ 'end_year'   ])
    
    urls = build_esearch_url_year_range(
        term      = name,
        from_year = start_year,
        to_year   = end_year
    )

    context = {
        'name'       : name,
        'start_year' : start_year,
        'end_year'   : end_year,
        'urls'       : urls,
    }
    
    response = HttpResponse(
        template.render(
            context, 
            request
        )
    )
    
    return response


