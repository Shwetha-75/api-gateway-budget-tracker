import requests
import os
class RegistrationServices:
      def register_activity(self,user_data):
          return requests.post(f"{os.getenv('REGISTER_SERVICES')}",json=user_data).json()
      
            