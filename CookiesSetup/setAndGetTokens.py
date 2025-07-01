import os 
import requests
from flask import jsonify
from dotenv import load_dotenv 
load_dotenv()

class SetAndGetTokens:
      def getToken(self):
            try:
                return requests.get(f"{os.getenv("GET_SET_TOKENS_URL")}/set-tokens").json()
            except Exception as exception:
               print("Some issues while getting response ",exception)
               return jsonify({'status':'no','message':'Some while getting response '})
       
      def checkToken(self,current_token):
            data={
                    os.getenv('ACCESS_TOKEN_KEY'):current_token
                 }
            try:
                 return requests.post(f"{os.getenv("GET_SET_TOKENS_URL")}/decode-token",json=data).json() 
                  
            except Exception as exception:
                 print("something went wrong while decoding the access token",exception)
                 return jsonify({'status':'no','exp':None})   
               
            
  
            