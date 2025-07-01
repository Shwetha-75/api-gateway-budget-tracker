import requests 
class EmailRequestAll:
      def __init__(self,cursor):
          self.cursor=cursor 
          self.data={}
      def fetchAllEmail(self):
          self.data=requests.get("http://localhost:7006/fetchAllEmail").json()
          