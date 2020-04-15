from django.contrib import admin
from .models import *

#Project Admin
class ProjectAdmin(admin.ModelAdmin):

    list_display    = ('user', 'name', 'duration','createdAt')
    list_filter     = ('user','createdAt',)
    search_fields   = ["name","duration"]

#Task Admin
class TaskAdmin(admin.ModelAdmin):

    list_display    = ('project','name', 'start_date', 'end_date', 'createdAt','assign')
    list_filter     = ('project','assign','start_date','end_date','createdAt',)
    search_fields   = ["name",]

#Task Admin
class SubtaskAdmin(admin.ModelAdmin):

    list_display    = ('task','name', 'start_date', 'end_date', 'createdAt')
    list_filter     = ('task','start_date','end_date','createdAt',)
    search_fields   = ["name",]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Subtask, SubtaskAdmin)
