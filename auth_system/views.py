from django.shortcuts import render
from .models import User
from django.http import HttpResponse, HttpResponseNotAllowed
import json
from datetime import datetime, timedelta
import jwt

def login(request):
    if request.method == 'POST':
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
            
            return HttpResponse(json.dumps({
                'message': 'Login succeed',
                'email': user.email,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'is_agent':user.is_agent,
                'token': token
            }), status=200)
        except User.DoesNotExist:
            return HttpResponse(json.dumps('invalid credential'), status=401)
    else:
        return HttpResponseNotAllowed(['POST'])
    
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        password = data.get('password')
        
        if User.objects.filter(email=email).exists():
            print('email address already exist')
            return HttpResponse(json.dumps('email address already exist'), status=409)
        else:
            new_user = User(email=email, firstname=firstname, lastname=lastname, password=password)
            new_user.save()
            print('user created')
            return HttpResponse(json.dumps('signup succeed'), status=200)
    else:
        return HttpResponseNotAllowed(['POST'])
