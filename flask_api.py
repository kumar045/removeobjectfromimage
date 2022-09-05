import json
from flask import Flask
from flask import request
from flask import Flask, jsonify
app = Flask(__name__)



@app.route('/query-course',methods=['GET'])
def query_example():
    # if key doesn't exist, returns None
    name = request.args.get('name')
    return jsonify({'name': name})
   

app.run(host ='0.0.0.0', port = 5000, debug = True) 
