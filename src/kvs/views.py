from django.shortcuts import render

# Create your views here.

# Code taken from django project's intro tutorial

import requests
import json

# Create your views here.

# Code taken from django project's intro tutorial and test_asgn2.py
from django.http import HttpResponse

keyValueStore = {} # In-memory storage of key-value pairings

def key(request, key):
    # Key can not be longer than 50 characters
    if len(key) > 50:
        # 400
        return HttpResponse(content = \
            json.dumps({"error":"Value is missing","message":"Error in PUT"}), \
            content_type = "application/json", status = 400)
    # Read the value of a key and return to client
    if request.method == 'GET':
        # Key DNE, so return error
        if keyValueStore.get(key) == None:
            # 404
            return HttpResponse(content = \
                json.dumps({"doesExist":False,"error":"Key does not exist","message":"Error in GET"}), \
                content_type = "application/json", status = 404)
        # Key exists, so return value
        else:
            # 200
            return HttpResponse(content = \
                json.dumps({"doesExist":True,"message":"Retrieved successfully","value":keyValueStore.get(key)}), \
                content_type = "application/json", status = 200)
    # Create or update a key-value pair
    elif request.method == 'PUT':
        try:
            values = json.loads(request.body)
        # Improperly formatted json data, return error
        except json.JSONDecodeError:
            # 400
            return HttpResponse(content = \
                json.dumps({"error":"Value is missing","message":"Error in PUT"}), \
                content_type = "application/json", status = 400)
        else:
            # Non-existent value, return error
            if values.get('value') == None:
                # 400
                return HttpResponse(content = \
                    json.dumps({"error":"Value is missing","message":"Error in PUT"}), \
                    content_type = "application/json", status = 400)
            # Key DNE, so create new pairing
            if keyValueStore.get(key) == None:
                # 201
                keyValueStore[key] = values.get('value')
                return HttpResponse(content = \
                    json.dumps({"message":"Added successfully","replaced":False}), \
                    content_type = "application/json", status = 201)
            # Key exists, so update pairing
            else:
                # 200
                keyValueStore[key] = values.get('value')
                return HttpResponse(content = \
                    json.dumps({"message":"Updated successfully","replaced":True}), \
                    content_type = "application/json", status = 200)
    # Delete a key-value pair
    elif request.method == 'DELETE':
        # Key DNE, so return error
        if keyValueStore.get(key) == None:
            # 404
            return HttpResponse(content = \
                json.dumps({"doesExist":False,"error":"Key does not exist","message":"Error in DELETE"}), \
                content_type = "application/json", status = 404)
        # Key exists, so delete pair
        else:
            # 200
            keyValueStore.pop(key)
            return HttpResponse(content = \
                json.dumps({"doesExist":True,"message":"Deleted successfully"}), \
                content_type = "application/json", status = 200)

    else:
        # 405
        return HttpResponse("This method is unsupported.", status=405)	
    return HttpResponse("You should never get here. Send help", status=500)	