from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
        url(r'^$', views.dashboard, name='dashboard'), 
        url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
        url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
]
