from django.shortcuts import render, render_to_response
from models import Service
from models import ServiceForm
from django.shortcuts import redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tongji.views import ServerList
from models import UploadFile
from forms import UploadFileForm
import subprocess
from django.core.urlresolvers import reverse
from django.template import RequestContext


# Create your views here.


@login_required
def service_list(request, template_name='deploy/service_list.html'):
    services = Service.objects.all()
    data = {}
    data['object_service'] = services
    data.update({'username': request.session['username']})
    return render(request, template_name, data)


@login_required
def service_create(request, template_name='deploy/service_form.html'):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        try:
            process = Service.objects.get(name=name)
        except Service.DoesNotExist:
            form.save()
            return redirect('service_list')
        else:
            return HttpResponse("Ip address is exist")
    return render(request, template_name, {'form': form, 'username': request.session['username']})


@login_required
def service_update(request, pk, template_name='deploy/service_form.html'):
    sevice = get_object_or_404(Service, pk=pk)
    form = ServiceForm(request.POST or None, instance=sevice)
    if form.is_valid():
        form.save()
        return redirect('service_list')
    return render(request, template_name, {'form': form, 'username': request.session['username']})


@login_required
def service_delete(request, pk, template_name='deploy/service_confirm_delete.html'):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, template_name, {'object': service, 'username': request.session['username']})


@login_required
def select_operate(request, template_name='deploy/operate2.html'):
    data = {}
    servers = ServerList.objects.all()
    services = Service.objects.all()
    data['object_server'] = servers
    data['object_service'] = services
    data['username'] = request.session['username']
    if request.method == 'POST':
        download_path = request.POST.get('download_path')
        target_path = request.POST.get('target_path')
        server_id = request.POST.get('pick_server')
        service_id = request.POST.get('pick_service')

        hosts = str(ServerList.objects.get(id=server_id).server_external_ip)
        user = str(ServerList.objects.get(id=server_id).server_admin)
        password = str(ServerList.objects.get(id=server_id).server_password)
        #task_name = str(Service.objects.get(id=service_id).name)
        task_name = "mysql_task"
        port = str(ServerList.objects.get(id=server_id).server_port)

        task_process = subprocess.Popen(['fab', '-f', '/Users/jack/PycharmProjects/OMServer/deploy/fabfiles/tasks.py',
                                        '-H', hosts, '-u', user, '-p', password, '--port', port, '-P',
                                         '%s:%s,%s' % (task_name, download_path, target_path)],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        data['task_process'] = task_process.communicate()
    return render(request, template_name, data)


@login_required
def edit_file(request, pk, template_name='deploy/file_update.html'):
    file_all = UploadFile.objects.get(pk=pk)
    file_path = file_all.script_file.path
    content = file_all.script_file.read()
    if request.method == 'POST':
        from django.core.files import File
        f = open(file_all.script_file.path, 'w')
        content = request.POST['content']
        f.write(content)
        f = File(f)
        file_all.source = f
        file_all.save()

    return render_to_response(template_name, {'file': file_path, 'content': content,
                                              'username': request.session['username']},
                              context_instance=RequestContext(request))


@login_required
def upload_scripts(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_script = UploadFile(script_file=request.FILES['script_file'])
            new_script.save()
            return HttpResponseRedirect(reverse('deploy.views.upload_scripts'))
    else:
        form = UploadFileForm()

    scripts = UploadFile.objects.all()

    return render_to_response('deploy/list.html', {'scripts': scripts, 'form': form,
                                                   'username': request.session['username']},
                              context_instance=RequestContext(request))
