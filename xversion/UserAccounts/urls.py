from .forms import MyAuthenticationForm
from . import views
from django.urls import re_path as url, include
from django.contrib.auth import views as auth_views, get_user_model

app_name = 'useraccounts'
User = get_user_model()
from django.contrib.auth.views import (LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView)
urlpatterns =[
    url(r'^home$', views.home,name='home'),
    url(r'^login/$', LoginView.as_view(authentication_form=MyAuthenticationForm,template_name='useraccounts/login.html'),name="login"),
    url(r'^logout/$', LogoutView.as_view(template_name='useraccounts/logout.html'), name='logout'),
    url(r'^signup/$', views.register, name='signup'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),


    #url('^', include('django.contrib.auth.urls')),

]
