"""Authentication viewset module."""
import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from listapi.serializers import UserSerializer

@csrf_exempt
def login_user(request):
    '''Handles the authentication of a player.
    Method arguments:
      request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    if request.method == 'POST':

        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            serializer = UserSerializer(authenticated_user, context={ 'request': request })
            login(request, authenticated_user)
            data = json.dumps({"valid": True, "token": token.key, "user": serializer.data})
            return HttpResponse(data, content_type='application/json')

        else:
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')

@csrf_exempt
def logout_user(request):
    '''Handles logging the user out.
    Method arguments:
      request -- The full HTTP request object
    '''

    logout(request)

@csrf_exempt
def register_user(request):
    '''Handles the creation of a new player for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name']
    )

    token = Token.objects.create(user=new_user)
    serializer = UserSerializer(new_user, context={ 'request': request })
    data = json.dumps({"valid": True, "token": token.key, "user": serializer.data})
    return HttpResponse(data, content_type='application/json')