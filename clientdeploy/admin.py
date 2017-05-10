from django.contrib import admin
from .models import ClientSyncSetting,SyncServer,ClientCategory

# Register your models here.
class ClientSyncSettingAdmin(admin.ModelAdmin):
    list_display = ('name','version_num','sync_server','category','sub_folder','shortcut_filename','program_filename','created','modified','is_active')

class SyncServerAdmin(admin.ModelAdmin):
    list_display = ('name','host','username','password','ssh_host_key_fingerprint')

class ClientCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','category_folder_name')

admin.site.register(ClientSyncSetting,ClientSyncSettingAdmin)
admin.site.register(SyncServer,SyncServerAdmin)
admin.site.register(ClientCategory,ClientCategoryAdmin)

