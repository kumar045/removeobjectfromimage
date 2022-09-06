from flask import request
from flask import Flask, jsonify
import http.client
import json
import logging
app = Flask(__name__)

@app.route('/users', methods = ['POST','GET']) 
def new_user():
    user_data = request.get_json() # 
    
    conn = http.client.HTTPSConnection("bs2ipcul0apon0jufi80lite.db2.cloud.ibm.com")
    # payload = "{\"commands\":\"select * from test1;\",\"limit\":10,\"separator\":\";\",\"stop_on_error\":\"yes\"}"
    lis = list(user_data['name'].split(" "))
    
    # length of list
    length = len(lis)
    
    # returning last element in list
    arg=lis[length-1]

    command="select * from test where Name="+ " '{}' ".format(arg)

    payload={"commands":command,"limit":10,"separator":";","stop_on_error":"no"}


    payload = json.dumps(payload, indent=2).encode('utf-8')


    headers = {
        'content-type': "application/json",
        'authorization': "Bearer eyJraWQiOiJXVEkxNjYwODc3MjcwNTQyUUtOSVJMaDVkUmEqLUhOSSpILTFiQnJKQVgrVFBkZWV0anJTM0pkc3IqVXg0OE5lYlZGSkxaN2MyaFNKTjU1YzJaM0xoKmRnSGNRYXZqZ0tkRThnWFJtQWNqQ3Y1Q1lEUlRoTndJandlU1BveUhtWm80ajdiWUkyaTNLZlVzTngwdFZHd2xzNXllTzJWRE05Qm14WFpOZkRDMlpNNjFCRTZKaUhIQ25yKlhGWWNpdkVDM2NRN2VWNVJOT0x4WG9tb0h0aHhFUHUxV09WeEdoUGJrQ2U0NHB6ZzhSaE5nTkFSTlV1M253UXBuNU5DNyplIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJodHRwczovL2xvY2FsaG9zdDo0NDMiLCJnZW5lcmF0ZVRpbWVzdGFtcCI6IjE2NjI0NDQ3MzUwNTAiLCJleHAiOjE2NjI0NzM1MzUsImV4cGlyZWRUaW1lIjoiMTY2MjQ3MzUzNTA1MCIsInVzZXJuYW1lIjoieGtkMjIwMzQifQ.WnxqFq7rznL5gzqDYedo2nDnjFkgUA-Ky8p9aZGdcNdX3UjOpF-R7S-Bn3TvJWF2nfUZ3gZM0_cvIUk-EFYTcgBkPvD69XZr1Ff0DDMuZE0IKwI74U_Pvjb9W29JGNb2HXb5lxRASrbslYr5SmOk7jtSgMqvLqemOhZ1rnTyGdUS3O5_8z_DZXEMxqVx9htlD2vONoGJNblwj5trVTZIh5FKIVxNzcQdtcRGFZ0I2LWu1xPkGx99cobPbRlRuOv2jDnl_Ssi-BcXyjicbskIrIAg8m5H0gPivn0iXHHpvCvuFA2XMRkUDwFf7cVqP8qgQUHKwxNVDyYijcLtyD9NLw",
        'x-deployment-id': "crn:v1:bluemix:public:dashdb-for-transactions:eu-gb:a/f1240aab988544deb28f2e7ea8740123:b515564c-124e-451f-9804-d4314aa7138a::"
        }
    conn.request("POST", "/dbapi/v4/sql_jobs", payload, headers)

    res = conn.getresponse()
    data = res.read()

    data=data.decode("utf-8")
    #To convert string to dictionary
    data= eval(data)

    conn.request("GET", "/dbapi/v4/sql_jobs/"+data["id"], headers=headers)

    res = conn.getresponse()
    data = res.read()
    data=data.decode("utf-8")
    data= eval(data)

    return jsonify(data)
app.run(host ='0.0.0.0', port = 5000, debug = True) 

