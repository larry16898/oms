from django.contrib import admin
from .models import ClientSyncSetting

# Register your models here.
class ClientSyncSettingAdmin(admin.ModelAdmin):
    list_display = ('name','version_num','parent_folder','sub_folder','host','username','password',
            'ssh_host_key_fingerprint','shortcut_filename','program_filename','created','modified')

admin.site.register(ClientSyncSetting,ClientSyncSettingAdmin)

