from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from construct_urls import build_esearch_url_year_range
from fetch_from_url \
    import \
        fetch_term_count_for_year, \
        fetch_term_count_for_year_range

# Create your views here.
def index(request):
    template = loader.get_template('get_input/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

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
    
    counts = fetch_term_count_for_year_range(name, start_year, end_year)
    #counts = {2002: 99330, 2003: 105142, 2004: 113432, 2005: 123584, 2006: 129036, 2007: 136862, 2008: 145089, 2009: 151514, 2010: 167665}
    #counts = {2010: 167665, 2011: 176218, 2012: 189013}
    #counts = {2016: 48206, 2017: 46524, 2018: 45747, 2019: 10114, 2000: 19884, 2001: 17126, 2002: 19357, 2003: 20404, 2004: 22801, 2005: 25695, 2006: 27313, 2007: 29323, 2008: 31572, 2009: 32714, 2010: 37064, 2011: 37906, 2012: 40813, 2013: 43809, 2014: 46551, 2015: 48083}
    #print(counts);

    
    context = {
        'name'         : name,
        'start_year'   : start_year,
        'end_year'     : end_year,
        'urls'         : urls,
        'counts'       : counts,
        'years_sorted' : sorted(counts.keys())
    }
    
    response = HttpResponse(
        template.render(
            context, 
            request
        )
    )
    
    return response


