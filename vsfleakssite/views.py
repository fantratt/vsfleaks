from django.shortcuts import *
from vsfleakssite.forms import *
from django.template import RequestContext
from vsfleakssite.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request, tag=None):
    posts = Post.objects.filter(published=True)
    if tag:
        posts = posts.filter(tags__name__in=[tag])
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    #render_to_response with context_instance
    return render(request, 'vsfleakssite/index.html', {'posts' : posts})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'vsfleakssite/post.html', {'post' : post})

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


    