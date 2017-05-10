from rest_framework import serializers
from .models import SyncServer,ClientCategory,ClientSyncSetting

class SyncServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyncServer
        fields = '__all__'

class ClientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCategory
        fields = '__all__'

class ClientSyncSettingSerializer(serializers.ModelSerializer):
    sync_server = SyncServerSerializer()
    category = ClientCategorySerializer()

    class Meta:
        model = ClientSyncSetting
        fields = ('name','version_num','category','sub_folder','sync_server',
                'shortcut_filename','program_filename','file_mask')

