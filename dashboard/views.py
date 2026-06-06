from django.shortcuts import render
from django.contrib.auth.decorators import login_required


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# from google import genai
# import os

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required(login_url='login')
def progress(request):
    return render(request, 'dashboard/progress.html')


@login_required(login_url='login')
def roadmap(request):
    return render(request, 'dashboard/roadmap.html')


@login_required(login_url='login')
def aichat(request):
    return render(request, 'dashboard/aichat.html')



#@csrf_exempt
# @login_required(login_url='login')
# def chat_api(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         user_message = data.get('message', '')
        

#         model = genai.GenerativeModel('gemini-2.5-flash')
#         response = model.generate_content(
#             f"Tu GoalBuddy ka AI career mentor hai. Indian students ki career guidance karta hai. Hinglish mein jawab de. User ka sawaal: {user_message}"
#         )

#         return JsonResponse({'reply': response.text})
#     return JsonResponse({'error': 'Invalid request'}, status=400)