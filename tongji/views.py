from django.shortcuts import render
from tongji.models import ServerList
from tongji.models import ContactForm
from django.http import HttpResponse


# Create your views here.
def server_info_submit(request):
    if request.method == 'POST':
        tj_forms = ContactForm(request.POST)
        if tj_forms.is_valid():
            server_external_ip = tj_forms.cleaned_data['server_external_ip']
            try:
                process = ServerList.objects.get(server_external_ip=server_external_ip)
            except ServerList.DoesNotExist:
                tj_forms.save()
                return HttpResponse("OK")
            else:
                return HttpResponse("%s address exist." %server_external_ip)
    else:
        tj_forms = ContactForm()
    return render(request, 'device_submit.html', {'form': tj_forms})

def server_info_display(request):
    items = ServerList.objects.all()
    return render(request, 'tongji.html', {'items': items})