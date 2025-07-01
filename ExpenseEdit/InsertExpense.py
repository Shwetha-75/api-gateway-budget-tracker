import requests
class InsertExpense:
      def insertExpense(self,data):
          return requests.post("http://localhost:4005/create",json=data).json()
          
