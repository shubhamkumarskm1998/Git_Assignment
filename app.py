from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MONGO_URI = "your_mongodb_atlas_uri"
client = MongoClient(MONGO_URI)

db = client["todo_db"]
collection = db["items"]

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    try:
        data = request.form   # from HTML form

        item = {
            "itemName": data.get("itemName"),
            "itemDescription": data.get("itemDescription")
        }

        collection.insert_one(item)

        return "Item added successfully"

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
