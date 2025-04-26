from flask import Flask,request,jsonify
from dotenv import load_dotenv 
from LoginServices.loginServices import LoginServices
load_dotenv()
import os

app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    return "ok"

@app.route("/login-service",methods=['POST','GET'])
def login_service():
    if request.method == 'POST':
       return LoginServices.loginActivity(user_data=dict(request.form))
    return jsonify({"status":"no"})


if __name__=='__main__':
  app.run(port=os.getenv('PORT'),debug=True)
