from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse
from tongji.models import ServerList
from tongji.models import ContactForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def server_list(request, template_name='servers/server_list.html'):
    servers = ServerList.objects.all()
    data = {}
    data['object_list'] = servers
    data.update({'username': request.session['username']})
    return render(request, template_name, data)

@login_required
def server_create(request, template_name='servers/server_form.html'):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        server_external_ip = form.cleaned_data['server_external_ip']
        try:
            process = ServerList.objects.get(server_external_ip=server_external_ip)
        except ServerList.DoesNotExist:
            form.save()
            return redirect('server_list')
        else:
            return HttpResponse("Ip address is exist")
    return render(request, template_name, {'form': form, 'username': request.session['username']})

@login_required
def server_update(request, pk, template_name='servers/server_form.html'):
    server = get_object_or_404(ServerList, pk=pk)
    form = ContactForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form': form, 'username': request.session['username']})

@login_required
def server_delete(request, pk, template_name='servers/server_confirm_delete.html'):
    server = get_object_or_404(ServerList, pk=pk)
    if request.method == 'POST':
        server.delete()
        return redirect('server_list')
    return render(request, template_name, {'object': server, 'username': request.session['username']})