# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response
from models import Service
from forms import ServiceForm
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
    data = {'object_service': services}
    data.update({'username': request.session['username']})
    return render(request, template_name, data)


@login_required
def service_create(request, template_name='deploy/service_form.html'):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['soft_name']
        try:
            process = Service.objects.get(soft_name=name)
        except Service.DoesNotExist:
            form.save()
            return redirect('service_list')
        else:
            return HttpResponse("%s is exist" % process)
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
        server_id = request.POST.get('pick_server')
        service_id = request.POST.get('pick_service')
        host = str(ServerList.objects.get(id=server_id).server_external_ip)
        user = str(ServerList.objects.get(id=server_id).server_admin)
        password = str(ServerList.objects.get(id=server_id).server_password)
        port = str(ServerList.objects.get(id=server_id).server_port)

        fabric_name = Service.objects.get(id=service_id).fabric_task
        script_type = Service.objects.get(id=service_id).script_type
        fabric_path = Service.objects.get(id=service_id).fabric_path
        fabric_script_name = Service.objects.get(id=service_id).fabric_script_name
        local_bash_path = Service.objects.get(id=service_id).local_bash_path
        local_bash_name = Service.objects.get(id=service_id).local_bash_name

        soft_version = request.POST.get('soft_version')
        download_path = request.POST.get('download_path')
        target_path = request.POST.get('target_path')

        task_process = subprocess.Popen(['fab', '-f', '%s/%s'
                                         % (fabric_path, fabric_script_name), '-H', host, '-u', user, '-p', password,
                                         '--port', port, '-P', '%s:%s,%s,%s,%s,%s,%s'
                                         % (fabric_name, download_path, target_path,
                                            soft_version, local_bash_path, local_bash_name, fabric_name)],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return_code = task_process.poll()
        return_list = []
        while return_code is None:
            line = task_process.stdout.readline()
            return_list.append(line)
            return_code = task_process.poll()
            line = line.strip()
            print line
        data['return_list'] = return_list

        if script_type == 'bash':
            if return_code == 0:
                data['task_process'] = "%s install success." % fabric_name
            else:
                data['task_process'] = "%s install failed. please check script." % fabric_name
        else:
            if return_code == 0:
                data['task_process'] = "%s install failed." % fabric_name
            else:
                data['task_process'] = "%s install success." % fabric_name
    return render(request, template_name, data)


@login_required
def edit_file(request, pk, template_name='deploy/file_update.html'):     # Edit file
    file_all = UploadFile.objects.get(pk=pk)
    filename = file_all.script_file.path
    content = file_all.script_file.read()
    if request.method == 'POST':
        from django.core.files import File
        f = open(file_all.script_file.path, 'w')
        content = request.POST.get('content')
        f.write(content)
        f = File(f)
        file_all.source = f
        file_all.save()

    return render_to_response(template_name, {'file': filename, 'content': content,
                                              'username': request.session['username']},
                              context_instance=RequestContext(request))


@login_required
def upload_scripts(request):     # File upload
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
