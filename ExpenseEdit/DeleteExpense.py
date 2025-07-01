import requests
class DeleteExpense:
      def deleteExpense(self,data):
          return requests.post("http://localhost:7006/delete-expense",json=data).json()