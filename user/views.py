from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse,HttpResponse,HttpRequest,HttpResponseBadRequest
import json
import simplejson
from .models import User
from django.db.models.query import QuerySet



def checkemail(request):
    pass

def reg(request:HttpRequest):

    # print(request,'~~~~~~~~~')
    try :
        payload = simplejson.loads(request.body)
        email = payload['email']
        # 数据库中是否含有

        qs = User.objects.filter(email=email)
        # print(mgr , type(mgr))
        print(qs.query)
        if qs: # 数据库已经存在
            return HttpResponseBadRequest()



        name = payload['name']
        password = payload['password']

        user = User()
        user.email = email
        user.name = name
        user.password = password
        # print(email,name,password)
        try:
            user.save()
            return JsonResponse({"user_id":user.id})
        except Exception as e:
            raise
        # return HttpResponse('welcome to register page')

    except Exception as e:
        return HttpResponseBadRequest()

