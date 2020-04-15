from django.urls import path, include, re_path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views, task_views, subtask_views

urlpatterns = [
    path('', views.project_list, name='project_list'), #fetch user's projects
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #user login
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),#user logout
    #project urls
    path('projects', views.project_list, name='project_list'),#fetch user's projects
    path('projects/add', views.project_add, name='project_add'),#add new project
    path('projects/edit/<int:pk>', views.project_edit, name='project_edit'),#edit project
    path('projects/view/<int:pk>', views.project_view, name='project_view'),#view project details
    path('projects/delete/<int:pk>', views.project_delete, name='project_delete'),#delete project
    #project's task urls
    path('project/<int:pid>/tasks', task_views.task_list, name='task_list'),#fetch project's tasks list
    path('project/<int:pid>/tasks/add', task_views.task_add, name='task_add'),#add new task
    path('project/<int:pid>/tasks/edit/<int:pk>', task_views.task_edit, name='task_edit'),#edit task
    path('project/<int:pid>/tasks/view/<int:pk>', task_views.task_view, name='task_view'),#view task details
    path('project/<int:pid>/tasks/delete/<int:pk>', task_views.task_delete, name='task_delete'),#delete task
    #task's subtask urls
    path('project/<int:pid>/task/<int:tid>/subtasks', subtask_views.subtask_list, name='subtask_list'),#fetch task's subtasks list
    path('project/<int:pid>/task/<int:tid>/subtasks/add', subtask_views.subtask_add, name='subtask_add'),#add new subtask
    path('project/<int:pid>/task/<int:tid>/subtasks/edit/<int:pk>', subtask_views.subtask_edit, name='subtask_edit'),#edit subtask
    path('project/<int:pid>/task/<int:tid>/subtasks/view/<int:pk>', subtask_views.subtask_view, name='subtask_view'),#view subtask details
    path('project/<int:pid>/task/<int:tid>/subtasks/delete/<int:pk>', subtask_views.subtask_delete, name='subtask_delete'),#delete subtask
]