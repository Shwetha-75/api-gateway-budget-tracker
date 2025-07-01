from CookiesSetup.setAndGetTokens import SetAndGetTokens
import json
from flask import make_response,jsonify
from dotenv import load_dotenv
import os
import base64 
load_dotenv()

cookie_domain=None

class CookiesSetup:
      def __init__(self):
          self.authorization=SetAndGetTokens()

      def setCookies(self,user_data):
          try:
            #   get the access toke after authenticating 
              access_token=self.authorization.getToken()
              print("ACCESS Token:",dict(access_token))
            #   payload is email
              payload={
                  'email':user_data['user_model']['email']
              }
            #   encrypting the payload
              secret_value=base64.urlsafe_b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')
              print("User Data : ",user_data)
              response=make_response(user_data)
            #   setting  the cookies
              response.set_cookie(
                   os.getenv('ACCESS_TOKEN_KEY'),
                   secret_value,
                   max_age=3600,
                   httponly=True,
                   samesite='Lax',
                   secure='False',
                   domain=cookie_domain
              )
            #   setting the access tokens on headers for authorizing the user 
              response.headers['Authorization']=f"{access_token[os.getenv('ACCESS_TOKEN_KEY')]}"
              response.headers['Access-Control-Expose-Headers'] = 'Authorization'
              response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000' 
              response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS' 
              response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization' 
              response.headers['Access-Control-Allow-Credentials']='true'
            #   print(response.headers['Authorization'])
              return response 
          
          except Exception as exception:
                 print("Some issues while cookies set up !!",exception)
                 return jsonify({'status':'no'})