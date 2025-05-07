from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def login(request):
  return HttpResponse("Hello World")
  if request.method == 'POST':
    try:
      data = json.load(request.body)
      username = data.get('username')
      password = data.get('password')
    except json.JSONDecodeError:
      return JsonResponse({"error": 'Invalid JSON'}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return JsonResponse({'message': 'Login successful', 'user_id':user.id , 'username': user.username})
    else: 
      return JsonResponse({'error': "Invalid credentials"}, status= 401)


