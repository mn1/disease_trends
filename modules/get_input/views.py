from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

from construct_urls import build_esearch_url_year_range
from fetch_from_url \
    import \
        fetch_term_count_for_year, \
        fetch_term_count_for_year_range

from django import forms

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
class DiseaseEntryForm(forms.Form):
    
    name       = forms.CharField(label='Disease',    max_length=100)
    start_year = forms.CharField(label='Start year', max_length=100)
    end_year   = forms.CharField(label='End year',   max_length=100)

    def clean(self):
        
        cleaned_data   = super().clean()
        start_year_str = cleaned_data.get("start_year")
        end_year_str   = cleaned_data.get("end_year")
        
        if not(RepresentsInt(start_year_str)):
            raise forms.ValidationError(
                "Start year must be an integer!"
            )
        
        start_year = int(start_year_str)
        
        if start_year < 1995:
            raise forms.ValidationError(
                "Start year must be at least 1995!"
            )
        if not(RepresentsInt(end_year_str)):
            raise forms.ValidationError(
                "End year must be an integer!"
            )

        end_year = int(end_year_str)

        if end_year > 2019:
            raise forms.ValidationError(
                "End year must not be later than 2019!"
            )

        if start_year>end_year:
            raise forms.ValidationError(
                "Start year must not be greater than end year!"
            )

# Create your views here.
def index(request):
        
    if request.method == 'POST':
        
        form = DiseaseEntryForm(request.POST)
        if form.is_valid():
            return response(request)
    else:
        form = DiseaseEntryForm()

    context = {
            'form'       : form,
            'draw_chart' : False
    }
    template = loader.get_template('get_input/index.html')
    
    return HttpResponse(template.render(context, request))

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def response(request):
    
    template = loader.get_template('get_input/index.html')
    
    name       =     request.POST[ 'name'       ]
    start_year = int(request.POST[ 'start_year' ])
    end_year   = int(request.POST[ 'end_year'   ])
    
    #return redirect('get_input:get_input')
    
    urls = build_esearch_url_year_range(
        term       = name,
        from_year  = start_year,
        to_year    = end_year
    )
    
    counts = fetch_term_count_for_year_range(name, start_year, end_year)
    #counts = {2002: 99330, 2003: 105142, 2004: 113432, 2005: 123584, 2006: 129036, 2007: 136862, 2008: 145089, 2009: 151514, 2010: 167665}
    #counts = {2010: 167665, 2011: 176218, 2012: 189013}
    #counts = {2016: 48206, 2017: 46524, 2018: 45747, 2019: 10114, 2000: 19884, 2001: 17126, 2002: 19357, 2003: 20404, 2004: 22801, 2005: 25695, 2006: 27313, 2007: 29323, 2008: 31572, 2009: 32714, 2010: 37064, 2011: 37906, 2012: 40813, 2013: 43809, 2014: 46551, 2015: 48083}
    #print(counts);

    if request.method == 'POST':
        form = DiseaseEntryForm(request.POST)
    else:
        form = DiseaseEntryForm()

    context = {
        'name'         : name,
        'start_year'   : start_year,
        'end_year'     : end_year,
        'urls'         : urls,
        'counts'       : counts,
        'years_sorted' : sorted(counts.keys()),
        'draw_chart'   : True,
        'form'         : form,
    }
    
    response = HttpResponse(
        template.render(
            context, 
            request
        )
    )
    return response