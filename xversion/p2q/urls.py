from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url, include
from django.urls import path

app_name = 'p2q'


urlpatterns = [
    #path('chat/', views.chat_view, name='chat_view'),
    path('process_image/', views.process_image, name='process_image'),
    path('result/', views.result_view, name='result_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


