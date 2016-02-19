from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,render,get_object_or_404
from django.template import Context, RequestContext
from models import *

# Create your views here.

@login_required
def tasklist(request):
    username = request.username
    if len(DBA.objects.filter(username=username)) == 0:
        user_id = User.objects.filter(username=username)
        lines = Task.objects.filter(creater=user_id).order_by("-id")
    else:
        lines = Task.objects.order_by("-id")
    paginator = Paginator(lines, 10)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        show_lines = paginator.page(1)
    except EmptyPage:
        show_lines = paginator.page(paginator.num_pages)
    return render_to_response('task_list.html', RequestContext(request, {'lines': show_lines}))
