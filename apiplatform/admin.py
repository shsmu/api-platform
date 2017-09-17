from django.contrib import admin
from .models import ApiCase, Api, Project, User
from .forms import ApiForm


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('projectid', 'name')
    fields = ('projectid', 'name')



class ApiCaseAdmin(admin.ModelAdmin):

    list_display = ('name', 'desc',  'content')


class ApiAdmin(admin.ModelAdmin):

    list_display = ('project_name', 'name', 'uri', 'reqdata', 'respdata', 'chk_field', 'expect_rst', 'timeout', )
    def project_name(self, obj):
        return obj.projectid.name

    search_fields = ('name', 'uri', )
    form = ApiForm
    fields = ('projectid', 'name', 'uri', 'mothod', 'contenttype', 'charset', 'reqdata', 'respdata', 'chk_field', 'expect_rst', 'timeout', 'userid')

admin.site.register(Project, ProjectAdmin)
admin.site.register(ApiCase, ApiCaseAdmin)
admin.site.register(Api, ApiAdmin)
admin.site.register(User)

# admin.site.register([Project, Api])