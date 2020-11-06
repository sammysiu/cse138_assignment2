from django.shortcuts import render

import requests
import json

# Create your views here.

# Code taken from django project's intro tutorial and test_asgn2.py
from django.http import HttpResponse

def msg(request, key, addr):
    if request.method == 'GET':
        try:
            result = requests.get('http://%s/kvs/%s'%(addr, key),                       \
                                headers = {"Content-Type": "application/json"}          \
                                , timeout = 5)
        except:
            # 503
            return HttpResponse(content = \
                json.dumps({"error":"Main instance is down","message":"Error in GET"}), \
                content_type = "application/json", status = 503)
    elif request.method == 'PUT':
        try:
            result = requests.put('http://%s/kvs/%s'%(addr, key),                       \
                                data = request.body,                                    \
                                headers = {"Content-Type": "application/json"}          \
                                , timeout = 5)
        except:
            # 503
            return HttpResponse(content =                                               \
                json.dumps({"error":"Main instance is down","message":"Error in PUT"}), \
                content_type = "application/json", status = 503)
    elif request.method == 'DELETE':
        try:
            result = requests.delete('http://%s/kvs/%s'%(addr, key),                    \
                                headers = {"Content-Type": "application/json"}          \
                                , timeout = 5)
        except:
            # 503
            return HttpResponse(content =                                                  \
                json.dumps({"error":"Main instance is down","message":"Error in DELETE"}), \
                content_type = "application/json", status = 503)
    else:
        # 405
        return HttpResponse("This method is unsupported.", status = 405)	
    return HttpResponse(content = result.text, content_type = "application/json", status = result.status_code)