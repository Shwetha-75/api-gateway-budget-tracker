import json 
import base64
import os
import requests
from functools import wraps
from flask import request,jsonify,make_response
from dotenv import load_dotenv
load_dotenv()

def authorization(f):
    @wraps(f)
    def authorizeTheUser(*args,**kwargs):
        try:
            global result
            # print(request.cookies.get(os.getenv('ACCESS_TOKEN_KEY')))
            print("Request Headers: ",request.headers.get("Authorization"))
            auth_header=request.headers.get('Authorization')
            if auth_header:
              #  verify the access token
                result=requests.get(f"{os.getenv('GET_SET_TOKENS_URL')}/decode-token",json={os.getenv('ACCESS_TOKEN_KEY'):auth_header}).json()
                secret_value=json.loads(base64.urlsafe_b64decode(request.cookies.get(os.getenv('ACCESS_TOKEN_KEY'))).decode('utf-8'))
                if result:
                    print(secret_value)
                    request.user_data={'status':'yes'}      
                    return f(*args, **kwargs)
            return jsonify({'status':'no'})       
        except Exception as exception:
            print("Access Token missing : ",exception)
            return jsonify({'status':'no'})
    return authorizeTheUser
                
    
# @app.route('/api/protected_resource')
# # @googleAuthRequired.google_auth_required
# def protected_resource(): 
#     try:
        
#         session_token=request.cookies.get(os.getenv('ACCESS_TOKEN_KEY'))
      
#         if session_token: 
#            secret_value=json.loads(base64.urlsafe_b64decode(session_token).decode('utf-8'))
           
#         response=make_response(jsonify({'status':'no'}))
#         response.set_cookie(os.getenv('ACCESS_TOKEN_KEY'),'',expires=0)
#         return response
#     except Exception:
#         response=make_response(jsonify({'status':'no'}))
#         response.set_cookie('cookie','',expires=0)
#         return response