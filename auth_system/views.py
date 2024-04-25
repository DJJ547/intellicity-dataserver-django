from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from datetime import datetime, timedelta
import jwt

@api_view(['POST'])
def login(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')
    try:
        user = User.objects.get(email=email, password=password)

        # generate JWT token
        payload = {
            'email': user.email,
            'exp': datetime.now() + timedelta(minutes=60)
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        return Response({
            'message': 'Login succeed',
            'email': user.email,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'is_agent':user.is_agent,
            'token': token
        }, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response('invalid credential', status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def signup(request):
    data = json.loads(request.body)
    email = data.get('email')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    password = data.get('password')
    
    if User.objects.filter(email=email).exists():
        return HttpResponse(json.dumps('email address already exist'), status=409)
    else:
        new_user = User(email=email, firstname=firstname, lastname=lastname, password=password)
        new_user.save()
        return HttpResponse(json.dumps('signup succeed'), status=status.HTTP_200_OK)
