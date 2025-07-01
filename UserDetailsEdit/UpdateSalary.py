import requests
class UpdateSalary:
      def updateSalary(self,data):
          return requests.post("http://localhost:4005/update-salary",json=data).json()