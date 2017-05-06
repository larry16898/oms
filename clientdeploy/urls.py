from django.conf.urls import url
from clientdeploy import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
        url(r'^all/$', views.ClientSettingList.as_view()),
        ]

urlpatterns = format_suffix_patterns(urlpatterns)

