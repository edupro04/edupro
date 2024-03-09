from django.db import models
from django.conf import settings

class EditorModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        template = 'User: {0.user}'
        return template.format(self)

