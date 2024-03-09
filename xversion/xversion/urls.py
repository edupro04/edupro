from django.contrib import admin
from django.urls import path
from django.urls import re_path as url, include

from p2q import views as ans
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from UserAccounts.forms import NewPasswordResetForm
from django.contrib.auth.views import (LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('UserAccounts.urls', namespace='useraccounts')),#replace uaccounts later above url
    url(r'^$', ans.index, name='index'),


    url(r'^p2q/', include('p2q.urls'), name='p2q'),
    url(r'^eqeditor/', include('eqeditor.urls'), name='eqeditor'),

    url(r'^password_reset/$', PasswordResetView.as_view(form_class=NewPasswordResetForm, template_name='registration/password_reset_form.html'), name='password_reset'),
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html') , name='password_reset_complete'),

##################################index page urls###################################
path('about-us/', TemplateView.as_view(template_name='booking/aindex/about_us.html'), name='about-us'),
path('contact-us/', TemplateView.as_view(template_name='booking/aindex/contactus.html'), name='contact-us'),
path('pricing-and-delivery/', TemplateView.as_view(template_name='booking/aindex/pricing_n_delivery.html'), name='pricing-delivery'),
path('privacy-policy/', TemplateView.as_view(template_name='booking/aindex/privacy_policy.html'), name='privacy-policy'),
path('refund-rules/', TemplateView.as_view(template_name='booking/aindex/refund_n_cancel.html'), name='refund-rules'),
path('terms-and-conditions/', TemplateView.as_view(template_name='booking/aindex/tnc.html'), name='terms-conditions'),
##################################index page urls ends###################################

    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),


    #path('', include('booking.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
