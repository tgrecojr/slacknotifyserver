from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/sendmessage",methods=['POST'])
def sendmessagetoslack():
    slackmessage = request.get_json()['message']
    return jsonify(code="SUCCESS")
