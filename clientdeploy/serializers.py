from rest_framework import serializers
from .models import ClientSyncSetting

class ClientSyncSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSyncSetting
        fields = ('name','version_num','parent_folder','sub_folder','host','username','password','ssh_host_key_fingerprint',
                'shortcut_filename','program_filename','file_mask')

