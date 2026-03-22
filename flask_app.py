from IPython.lib.pretty import Printable
from flask import Flask, request, render_template, jsonify
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Create a new client and connect to the server
MONGO_URI = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db=client.test
collection=db['flask_tutorial']

app = Flask(__name__,template_folder="templates")
date=datetime.now().strftime("%A")
print(date)

@app.route("/")
def home():
    return render_template("index.html",day_of_week=date)

@app.route("/submit",methods=["POST"])
def submit():
    form_data=dict(request.form)
    print(form_data)
    collection.insert_one(form_data)
    return "Success"

@app.route("/api")
def name():
    name=request.values.get("name")
    age=request.values.get("age")
    result={"name":name,"age":age}
    return result

@app.route("/view")
def view():
    data=collection.find()
    data=list(data)
    for item in data:
        print(item)
        del item['_id']
    data={'data':data}
    return data

if __name__=='__main__':
    app.run(debug=True,use_reloader=False)