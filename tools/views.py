#-*- coding:utf-8 -*-

from django.shortcuts import render
#from django.db import connection
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template import Context, RequestContext
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required
from .models import LoginForm
from .models import ChangePasswordForm
from django.contrib.sessions.models import Session

# Create your views here.

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form, }))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    request.session['id'] = user.id
                    request.session['username'] = user.username
                    request.session['password'] = user.password
                    return HttpResponseRedirect('/index/')
            else:
                return render_to_response('login.html',
                                          RequestContext(request, {'from': form, 'password_is_wrong': True}))
        else:
            return render_to_response('login.html', RequestContext(request, {'form': form, }))

@login_required
def logout(request):
    auth.logout(request)
    try:
        del request.session['session_id']
    except KeyError:
        pass
    return HttpResponseRedirect("/accounts/login/")

@login_required
def changepassword(request):
    if request.session['id'] is not None:
        if request.method == 'GET':
            form = ChangePasswordForm()
            return render_to_response('change_password.html', RequestContext(request, {'form': form, }))
        else:
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                username = request.user.username
                #print username
                #old_password = request.POST.get('old_password', '')
                old_password = form.cleaned_data['old_password']
                #print old_password
                user = auth.authenticate(username=username, password=old_password)
                print user
                if user is not None:
                    if user.is_active:
                        new_password = request.POST.get('new_password', '')
                        print new_password
                        user.set_password(new_password)
                        user.save()
                        return render_to_response('index.html',
                                                  RequestContext(request, {'change_password_success': True}))
                else:
                    return render_to_response('change_password.html',
                                              RequestContext(request, {'form': form, 'old_password_is_wrong': True,
                                                                       'session_id': request.session['id'],
                                                                       'username': username,
                                                                       'old_password': old_password}))
            else:
               return render_to_response('change_password.html',
                                         RequestContext(request, {'form': form, 'session_id': request.session['id'],
                                                                  'username': request.session['username']}))
    else:
        return HttpResponseRedirect("/accounts/login/")

@login_required
def index(request):
    if request.session['id'] is not None:
        username = (request.session['username'])
        return render_to_response('index.html', RequestContext(request, {'session_id': request.session['id'],
                                                                         'username': username}))

    else:
        return HttpResponseRedirect("/accounts/login/")
