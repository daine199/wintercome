from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

from .models import CmdTask, RunLevel, WinterUser
from .forms import SignUpForm
from .lib import MACRO, common
import json


def basic_cmd_run(request, cmd_id):
    context = {}
    cmdtask = CmdTask.objects.get(id=int(cmd_id))
    res = cmdtask.base_call()
    context['task'] = cmdtask
    context['code'] = res['return_code']
    context['result'] = res['return_print']
    return render(request, 'wintercome/runresult.html', context)


def cmd_index_page(request):
    context = {}
    cmd_task_list = CmdTask.objects.all()
    context['cmd_task_list'] = cmd_task_list
    return render(request, 'wintercome/cmdlist.html', context)


def sign_up_page(request):
    context = {}
    form = SignUpForm()
    context['form'] = form
    return render(request, 'wintercome/signup.html', context)


def login_page(request):
    context = {}
    if request.session.get('userid', False):
        form = SignUpForm()
        context['form'] = form
        return render(request, 'wintercome/login.html', context)
    else:
        userid = request.session.get('userid')
        runlevel = request.session.get('runlevel')
        context['userid'] = userid
        if runlevel == MACRO.ADMINISTRATOR:
            context['user_list'] = True
        return render(request, 'wintercome/login.html', context)





def user_list_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            uid = form.cleaned_data['userid']
            pwd = form.cleaned_data['passwd']
            userinfo = WinterUser.objects.get(userid=uid)
            if pwd == userinfo.passwd:
                request.session['userid'] = uid
                request.session['level'] = userinfo.run_level
                return render(request, 'wintercome/userlist.html', context={})

            else:
                return HttpResponseRedirect('/wintercome/login/')
    else:
        pass

