from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from openai import OpenAI
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from UserAccounts.forms import MyAuthenticationForm

client = OpenAI(api_key=settings.OPENAI_API_KEY)

User = get_user_model()

def index(request):
    form = MyAuthenticationForm()
    return render(request, 'p2q/aindex/index.html', {'form': form})


def generate_questions(query):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Create questions based on the following text: {query}"},
            ],
            temperature=0.2,
            max_tokens=20,
        )

        # Extract and return the generated questions
        generated_text = response.choices[0].message.content
        generated_questions = generated_text.split('\n')
        return {'questions': generated_questions}
    except Exception as e:
        return {'error': str(e)}


def result_view(request):
    if request.method == 'POST':
        query = request.POST.get('user_input', '')
        word_count = len(query.split())

        if word_count > 500:
            if request.user.is_authenticated:
                try:
                    generated_questions = generate_questions(query)
                    if 'error' in generated_questions:
                        return JsonResponse({'error': generated_questions['error']})
                    return render(request, 'p2q/aindex/result.html', {'query': query, 'generated_questions': generated_questions['questions']})
                except Exception as e:
                    return JsonResponse({'error': str(e)})
            else:
                return render(request, 'p2q/aindex/index.html')
        else:
            try:
                generated_questions = generate_questions(query)
                if 'error' in generated_questions:
                    return JsonResponse({'error': generated_questions['error']})
                return render(request, 'p2q/aindex/result.html', {'query': query, 'generated_questions': generated_questions['questions']})
            except Exception as e:
                return JsonResponse({'error': str(e)})

    return render(request, 'p2q/aindex/index.html', {'query': '', 'generated_questions': ''})


@csrf_exempt
def process_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        print('inside process image')
        # Use PIL to open the image
        image = Image.open(uploaded_image)

        # Use Tesseract to extract text
        extracted_text = pytesseract.image_to_string(image)

        return JsonResponse({'text': extracted_text})

    return JsonResponse({'error': 'Invalid request'})
