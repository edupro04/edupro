from django import forms
from tinymce.widgets import TinyMCE
from .models import EditorModel


class EditorForm(forms.ModelForm):
    class Meta:
        model = EditorModel
        fields = ['content']
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }
