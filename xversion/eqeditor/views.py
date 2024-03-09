from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import EditorModel
from .forms import EditorForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


@login_required
def editorMain(request):
    #initial_text = "This is the initial text."
    user_content = EditorModel.objects.filter(user=request.user)
    form = EditorForm()

    return render(request, 'eqeditor/editor_main.html', {'user_content': user_content, 'form': form})

def get_content_api(request, content_id):
    print('inside api')
    content = get_object_or_404(EditorModel, id=content_id, user=request.user)
    return JsonResponse({'content': content.content})


@require_POST
def save_to_database(request):
    form = EditorForm(request.POST)
    print('working.....')
    if form.is_valid():
        form.instance.user = request.user
        instance = form.save()
        #return HttpResponse(request)
        return JsonResponse({'status': 'success', 'id': instance.id})
    else:
        print(form.errors)
        return JsonResponse({'status': 'error', 'errors': form.errors})
