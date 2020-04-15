from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http.response import  HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.cache  import cache_control
from .models import *
from .forms import TaskForm

#task listing
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def task_list(request, pid, template_name='task/list.html'):
    try:
        context                     = {}
        context['project']          = get_object_or_404(Project, pk=pid, user= request.user)
        context['object_list']      = Task.objects.filter(project__id= pid, project__user= request.user).order_by('-id')
        return render(request, template_name, context)
    except Exception as e:
            return e

#task add
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def task_add(request, pid, template_name='task/add.html'):
    try:
        project = get_object_or_404(Project, pk=pid, user= request.user)
        if request.method == 'POST':
                form = TaskForm(request.POST, project=project)
                if form.is_valid():
                        form.save()
                        messages.success(request,"Task has been successfully added.")
                        return redirect('/project/'+str(pid)+'/tasks')
        else:
                form  = TaskForm(request.POST or None, project=project)

        return render(request, template_name, {'form':form,'project':project})
    except Exception as e:
            return e

#task edit
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def task_edit(request, pid, pk, template_name='task/edit.html'):
    try:
        project = get_object_or_404(Project, pk=pid, user= request.user)
        task    = get_object_or_404(Task, pk=pk, project__id = pid)
        
        if request.method == 'POST':
                form = TaskForm(request.POST, instance=task, project=project)
                if form.is_valid():
                        form.save()
                        messages.success(request,"Task has been successfully updated.")
                        return redirect('/project/'+str(pid)+'/tasks/edit/'+str(pk))
        else:
                form  = TaskForm(request.POST or None, instance=task, project=project)

        return render(request, template_name, {'form':form,'project':project,'object':task})
    except Exception as e:
            return e

#task view
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def task_view(request, pid, pk, template_name='task/detail.html'):
    try:
        project = get_object_or_404(Project, pk=pid, user= request.user)
        task    = get_object_or_404(Task, pk=pk, project__id = pid, project__user= request.user)
        return render(request, template_name, {'object':task,'project':project})
    except Exception as e:
        return e

#task delete
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def task_delete(request, pid, pk, template_name='task/confirm_delete.html'):
    try:
        project = get_object_or_404(Project, pk=pid, user= request.user)
        task    = get_object_or_404(Task, pk=pk, project__id = pid, project__user= request.user)
        if request.method == 'POST':
                task.delete()
                messages.success(request,"Task has been successfully delete.")
                return redirect('/project/'+str(pid)+'/tasks')

        return render(request, template_name, {'object':task,'project':project})
    except Exception as e:
            return e


