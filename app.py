from flask import Flask,request,jsonify,json
from dotenv import load_dotenv 
# from LoginServices.loginServices import LoginServices
from LoginServices.LoginMainActivity import LoginMainActivity
from Registration.registrationServices import RegistrationServices
# from Configuration.config import *
from flask_cors import CORS 
from UserDetailsEdit.UpdateSalary import UpdateSalary
from ExpenseEdit.InsertExpense import InsertExpense
from ExpenseEdit.DeleteExpense import DeleteExpense
from Authorization.Authorization import authorization
load_dotenv()
import os

app=Flask(__name__)
CORS(app,supports_credentials=True, origins={r'/*':{"origins":[os.getenv('FRONT_END_1'),
os.getenv('FRONT_END_2'),
os.getenv('FRONT_END_3'),
os.getenv('FRONT_END_4'),
os.getenv('LOGIN_SERVICES'),
os.getenv('FRONT_END_5')]}})
# database=Configuration().get_database()


@app.route("/",methods=['POST','GET'])
def index():
    return "ok"

@app.route("/login-service",methods=['POST','GET'])
def login_service():
    if request.method == 'POST':
        # check if the json exist
        try:
            if request.get_json(): 
                # authenticate user data  
               result=LoginMainActivity().authenticateUser(request.get_json())
               return result
        except Exception as exception:
            print("Something went wrong",exception)
            
    return jsonify({        
        "status":"no",
        "message":"something went wrong",
        "user_model":None
        })
# testing 

@app.route("/check-user",methods=['POST','GET'])
@authorization
def checkUserDetails():
  
    user_data=request.user_data
    print(user_data)
    return "ok"
    
@app.route("/logout",methods=['GET','POST'])

# ---------------------------
@app.route("/register-services",methods=['POST','GET'])
def register_service():
    if request.method == 'POST':
       return RegistrationServices().register_activity(dict(request.form) if request.form else request.get_json())
    return jsonify({"status":"no"})

@app.route("/salary-update",methods=['POST','GET'])
@authorization
def updatingSalary():
    if request.method=='POST':
        print(request.user_data)
        data=dict(request.form)
        return UpdateSalary().updateSalary(data) 
@app.route("/add-expense",methods=['POST','GET'])
def addExpense():
    if request.method=='POST':
        data=dict(request.form)
        data['expense']=json.loads(data['expense'])
        print(data)
        return InsertExpense().insertExpense(data)
    return "Created !!"
@app.route("/delete-expense",methods=['POST','GET'])
def deleteExpense():
    if request.method=='POST':
        data=dict(request.form)
        return DeleteExpense().deleteExpense(data)
    return "Deleted !!"
if __name__=='__main__':
  app.run(host='0.0.0.0',port=os.getenv('PORT'),debug=True)

