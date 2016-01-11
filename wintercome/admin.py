from django.contrib import admin
from .models import CmdTask, RunLevel, WinterUser
# Register your models here.

# class cmdTaskInline(admin.StackedInline):
#     model = CmdTask
#     extra = 3


class RunLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'level')


class WinterUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'userid', 'run_level', 'passwd')


class CmdTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'ownerid', 'cmd', 'run_level')

admin.site.register(CmdTask, CmdTaskAdmin)
admin.site.register(WinterUser, WinterUserAdmin)
admin.site.register(RunLevel, RunLevelAdmin)
