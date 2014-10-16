from django.shortcuts import *
from vsfleakssite.forms import *
from django.template import RequestContext
from vsfleakssite.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def report(request):
    context = RequestContext(request)
    if request.method == 'POST':
        report_form = ReportForm(request.POST, request.FILES)
        if report_form.is_valid():
            print('saving')
            report_form.save()
            return redirect('vsfleaks:result')
    else:
        report_form = ReportForm()    
    return render_to_response('vsfleakssite/report.html', { 'report_form' : report_form } , context)
    
def result(request):
    context = RequestContext(request)
    return render_to_response('vsfleakssite/result.html', {}, context)


    