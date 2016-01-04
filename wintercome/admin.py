from django.contrib import admin
from .models import cmdTask,groupLevel,winterUser
# Register your models here.

# class cmdTaskInline(admin.StackedInline):
#     model = cmdTask
#     extra = 3

class groupLevelAdmin(admin.ModelAdmin):
    list_display = ('id','title','level')

class winterUserAdmin(admin.ModelAdmin):
    list_display = ('id','userid','group','passwd')

class cmdTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner','cmd','runlevel')

admin.site.register(cmdTask,cmdTaskAdmin)
admin.site.register(winterUser,winterUserAdmin)
admin.site.register(groupLevel,groupLevelAdmin)