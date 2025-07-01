# firebase admin 
import firebase_admin
# credentials,auth,firestore 
from firebase_admin import credentials,auth,firestore 

    
class Configuration:
    def __init__(self):
        cred=credentials.Certificate(r"E:\Budget-Manager\API-Gateway\Configuration\database.json")
        firebase_admin.initialize_app(cred)
        self.db=firestore.client()
    def get_database(self):
        return self.db
    
if __name__=='__main__':
    pass