from django.shortcuts import render
from manage_hotel.models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse
import traceback
import json
import base64
import os
from django.conf import settings
import logging


def owner_signup(request):
    '''register hotel owner'''
    try:
        data=request.data
        first_name=data['first_name']
        last_name=data['last_name']
        
        if 'age' in data:
           age=data['age']
        else:
            age=None
        
        email=data['email']
        check_user=User.objects.filter(email=email).exists()
        if check_user:
            return HttpResponse(json.dumps({
                "status":"success",
                "massage":"User with same email already exists"
            }))

        contact=data['contact']
        username=email
        password=data['password']

        if 'description' in data:
            description=data['description']
        else:
            description=''
        if 'city' in data:
            city=data['city']
        else:
            city=''
        
        if 'distict' in data:
            distict=data['distict']
        else:
            distict=''
        
        if 'state' in data:
            state=data['state']
        else:
            state=''
    


        user_obj=User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
            is_active=True
        )
        user_obj.save()

        owner_obj=hotel_owner_details(
            first_name=first_name,
            last_name=last_name,
            age=age,
            contact=contact,
            email=email,
            description=description,
            city=city,
            distict=distict,
            state=state
        )
        owner_obj.save()

        return HttpResponse(json.dumps({
                "status":"success",
                "massage":"Owner Registered successfully"
            }))

    except Exception as msg:
        # logger.error("wrong",exc_info=True)
        traceback.print_exc()
        return HttpResponse(json.dumps({
                "status":"failed",
                "massage":"There is backend issue, please contact administrator"
            }))



        