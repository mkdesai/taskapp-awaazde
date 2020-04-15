from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http.response import  HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.cache  import cache_control
from .models import *
from .forms import SubtaskForm

#subtask listing
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subtask_list(request, pid, tid, template_name='subtask/list.html'):
    try:
        context                     = {}
        project                     = get_object_or_404(Project, pk=pid, user= request.user)
        task                        = get_object_or_404(Task, pk=tid, project=project)
        context['project']          = project
        context['task']             = task
        context['object_list']      = Subtask.objects.filter(task=task).order_by('-id')
        return render(request, template_name, context)
    except Exception as e:
            return e

#subtask add
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subtask_add(request, pid, tid, template_name='subtask/add.html'):
    try:
        project = get_object_or_404(Project, pk=pid, user= request.user)
        task    = get_object_or_404(Task, pk=tid, project=project)
        if request.method == 'POST':
                form = SubtaskForm(request.POST, task=task)
                if form.is_valid():
                        form.save()
                        messages.success(request,"SubTask has been successfully added.")
                        return redirect('/project/'+str(pid)+'/task/'+str(tid)+'/subtasks')
        else:
                form  = SubtaskForm(request.POST or None, task=task)

        return render(request, template_name, {'form':form,'project':project,'task':task})
    except Exception as e:
            return e

#subtask edit
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subtask_edit(request, pid, tid, pk, template_name='subtask/edit.html'):
    try:
        project     = get_object_or_404(Project, pk=pid, user= request.user)
        task        = get_object_or_404(Task, pk=tid, project=project)
        subtask     = get_object_or_404(Subtask, pk=pk, task=task)
        
        if request.method == 'POST':
                form = SubtaskForm(request.POST, instance=subtask, task=task)
                if form.is_valid():
                        form.save()
                        messages.success(request,"SubTask has been successfully updated.")
                        return redirect('/project/'+str(pid)+'/task/'+str(tid)+'/subtasks/edit/'+str(pk))
        else:
                form  = SubtaskForm(request.POST or None, instance=subtask, task=task)

        return render(request, template_name, {'form':form,'project':project,'task':task,'object':subtask})
    except Exception as e:
            return e

#subtask view
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subtask_view(request, pid, tid, pk, template_name='subtask/detail.html'):
    try:
        project     = get_object_or_404(Project, pk=pid, user= request.user)
        task        = get_object_or_404(Task, pk=tid, project=project)
        subtask     = get_object_or_404(Subtask, pk=pk, task=task)
        return render(request, template_name, {'object':subtask,'project':project,'task':task})
    except Exception as e:
        return e

#subtask delete
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subtask_delete(request, pid, tid, pk, template_name='subtask/confirm_delete.html'):
    try:
        project     = get_object_or_404(Project, pk=pid, user= request.user)
        task        = get_object_or_404(Task, pk=tid, project=project)
        subtask     = get_object_or_404(Subtask, pk=pk, task=task)
        if request.method == 'POST':
                subtask.delete()
                messages.success(request,"SubTask has been successfully delete.")
                return redirect('/project/'+str(pid)+'/task/'+str(tid)+'/subtasks')
        return render(request, template_name, {'object':subtask,'project':project,'task':task})
    except Exception as e:
            return e


