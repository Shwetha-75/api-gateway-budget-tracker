import requests 
import os

class LoginServices:
    
      def loginActivity(self,data):
          return requests.post(f"{os.getenv('LOGIN_SERVICES')}/signin/auth/google",json=data).json()
      