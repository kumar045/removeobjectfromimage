import json
from flask import Flask
from flask import request
from flask import Flask, jsonify
import http.client
import json
import logging
app = Flask(__name__)

@app.route('/users', methods = ['POST','GET']) 
def new_user():
    user_data = request.get_json() # 
    print(user_data)
    conn = http.client.HTTPSConnection("bs2ipcul0apon0jufi80lite.db2.cloud.ibm.com")
    payload = "{\"commands\":\"select * from test1;\",\"limit\":10,\"separator\":\";\",\"stop_on_error\":\"yes\"}"

    
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer eyJraWQiOiJXVEkxNjYwODc3MTQwOTgxRFFWanhPKmJhQVlQY0tlWXRWeDZIdU5HTDRRak50VVBZY2lONlhjMlBvMENDeVA3NDhzVmczTjJyK2R5TWw1aVZRRXY1VSppM2RuVHRSeFZEbzhPUytNdnppUGhyLUpwOTIzZUQ5cVFFOUxiZ0VzWjlWUHZoUHVVeUVweTJEZ05EcFlZeTBsODEwZWUqYXpxVjdJZ2RtdXdSKkRSdzlnK1V1UVV5Z0hkYTI3a2N6N0QrZkhQVyp6LVY5WEFIb2NJaXNpbFlwNmFDT3ZmdzAxdEtRZkthbWtrNEdDRlVETERHclpIOU5lcG5tSWFRbUVFIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJodHRwczovL2xvY2FsaG9zdDo0NDMiLCJnZW5lcmF0ZVRpbWVzdGFtcCI6IjE2NjIzNjk1OTA0MzkiLCJleHAiOjE2NjIzOTgzOTAsImV4cGlyZWRUaW1lIjoiMTY2MjM5ODM5MDQzOSIsInVzZXJuYW1lIjoieGtkMjIwMzQifQ.hUxd0U8AAItP3e_PVFoRDcQ_TL_En6Ox6P5qaZxvVSJB6_c_zUI4bt-w2uvcUrGeiPJgpL1Qjge0TcGzcdKjTK38PkA75KUFLVoi4B-pi93zVgTSe4Q4kVERxJceBAvT8TLttqujjJhcKdWqFQYBGuscfmwzOdm3YwZR0U5z1L-Ws4CIlD7JWniYz-MbMvi9zsfzKS5rE1fnZk4OnwHlWEJ57XKmg-8KJxwSEsbo7UM6HH-BXnBqwxcVxC8Yi8Yc4H_hLxnY2NnbOJbD4kx_oaWlaO268XMmDkFznoiEk8DGRAj9Fe6A1QR7Wm3FOdcxYISr8OqOM7w_wLV9oyL09Q",
        'x-deployment-id': "crn:v1:bluemix:public:dashdb-for-transactions:eu-gb:a/f1240aab988544deb28f2e7ea8740123:b515564c-124e-451f-9804-d4314aa7138a::"
        }
    conn.request("POST", "/dbapi/v4/sql_jobs", payload, headers)

    res = conn.getresponse()
    data = res.read()

    data=data.decode("utf-8")
    #To convert string to dictionary
    data= eval(data)
    print(data["id"])
    conn.request("GET", "/dbapi/v4/sql_jobs/"+str(data["id"]), headers=headers)

    res = conn.getresponse()
    data = res.read()
    data=data.decode("utf-8")
    data= eval(data)

    # data=data["results"][0]["rows"]
        
  
    return jsonify({'name': data})
app.run(host ='0.0.0.0', port = 5000, debug = True) 
