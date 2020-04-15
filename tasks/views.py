from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http.response import  HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.cache  import cache_control
from .models import *
from .forms import ProjectForm
import os

#project listing
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def project_list(request, template_name='project/list.html'):
    try:
        context                     = {}
        context['object_list']      = Project.objects.filter(user= request.user).order_by('-id')
        return render(request, template_name, context)
    except Exception as e:
            return e

#project add
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def project_add(request, template_name='project/add.html'):
    try:
        ALLOWED_TYPES           = ['jpg', 'jpeg','png', 'JPG', 'JPEG', 'PNG']
        image_validation        = True       
        if request.method == 'POST':
                if request.FILES:
                        file_avatar = request.FILES.get('avatar', None)
                        extension = os.path.splitext(file_avatar.name)[1][1:].lower()
                        if extension not in ALLOWED_TYPES:
                                messages.error(request, 'Image types is not allowed')
                                image_validation = False
                
                form = ProjectForm(request.POST, request.FILES, user=request.user)
                if form.is_valid() and image_validation:
                        form.save()
                        messages.success(request,"Project has been successfully added.")
                        return redirect('/projects')
        else:
                form  = ProjectForm(request.POST or None, user=request.user)

        return render(request, template_name, {'form':form})
    except Exception as e:
            return e

#project edit
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def project_edit(request, pk, template_name='project/edit.html'):
    try:
        ALLOWED_TYPES           = ['jpg', 'jpeg','png', 'JPG', 'JPEG', 'PNG']
        image_validation        = True
        project                 = get_object_or_404(Project, pk=pk, user= request.user)
        if request.method == 'POST':
                if request.FILES:
                        file_avatar = request.FILES.get('avatar', None)
                        extension = os.path.splitext(file_avatar.name)[1][1:].lower()
                        if extension not in ALLOWED_TYPES:
                                messages.error(request, 'Image types is not allowed')
                                image_validation = False

                form = ProjectForm(request.POST, request.FILES, instance=project, user=request.user)
                if form.is_valid() and image_validation:
                        form.save()
                        messages.success(request,"Project has been successfully updated.")
                        return redirect('/projects/edit/'+str(pk))
        else:
                form  = ProjectForm(request.POST or None, instance=project, user=request.user)

        return render(request, template_name, {'form':form,'object':project})
    except Exception as e:
            return e

#project view
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def project_view(request, pk, template_name='project/detail.html'):
    try:
            project = get_object_or_404(Project, pk=pk, user= request.user)
            return render(request, template_name, {'object':project})
    except Exception as e:
            return e

#project delete
@login_required(login_url='/login') # - if not logged in redirect to /
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def project_delete(request, pk, template_name='project/confirm_delete.html'):
    try:
        project = get_object_or_404(Project, pk=pk, user= request.user)
        
        if request.method == 'POST':
                project.delete()
                messages.success(request,"Project has been successfully delete.")
                return redirect('/projects')

        return render(request, template_name, {'object':project})
    except Exception as e:
            return e


