from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ClientSyncSetting
from .serializers import ClientSyncSettingSerializer
from django.shortcuts import render

# Create your views here.
#@api_view(['GET',])
#def client_setting_list(request, format=None):
#    client_settings = ClientSyncSetting.objects.all()
#    serializer = ClientSyncSettingSerializer(client_settings, many=True)
#    return Response(serializer.data)
class ClientSettingList(APIView):
    def get(self, request, format=None):
        client_settings = ClientSyncSetting.objects.filter(is_active=True)
        serializer = ClientSyncSettingSerializer(client_settings, many=True)
        return Response(serializer.data)
