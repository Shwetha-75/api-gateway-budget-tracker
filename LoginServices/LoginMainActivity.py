from CookiesSetup.CookiesSetup import CookiesSetup
from LoginServices.loginServices import LoginServices
from flask import jsonify

class LoginMainActivity:
      def __init__(self):
          self.cookies=CookiesSetup()
          self.loginServices=LoginServices()
      def authenticateUser(self,user_data):
          try:
              result=self.loginServices.loginActivity(user_data)
              
              '''
              Sample of getting user data from Google sing in Services after insertion/ checking userdata 
              
               {
               'message': 'inserted', 
               'status': 'yes', 
               'user_model': {
                   'email': 'kshwetha676@gmail.com', 
                   'expenditure': [], 
                   'expenseAmt': 0, 
                   'f_name': 'Shwetha', 
                   'l_name': 'K', 
                   'm_name': '', 
                   'phone': 0, 
                   'picture': '', 
                   'salary': 0, 
                   'savings': 0
                   }
                }
              '''
            #   if the operation on database insert or read was successful
              if result['status']=='yes':
                # set up the cookies for payload email from user credential 
                # result contain the properties for the frm above 
                 return self.cookies.setCookies(result)
                 
          except Exception as exception:
              print("Something went while authenticating user ",exception)
              return jsonify({
              'status':'no',
              "message":"something went wrong",
              "user_model":None
              })
              