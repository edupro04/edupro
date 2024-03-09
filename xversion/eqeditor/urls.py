from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url, include, path

app_name = 'eqeditor'


urlpatterns = [
    url(r'^main/$', views.editorMain, name='editor_main'),
    path('api/get_content/<int:content_id>/', views.get_content_api, name='get_content_api'),
    path('save_to_database/', views.save_to_database, name='save_to_database'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


