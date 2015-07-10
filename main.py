from bottle import route, run, template
from bottle import route, request, response, template, HTTPResponse
import uuid
from bottle import static_file
import csv
import random
import json

auth_flag = 0

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="static")

@route('/')
def index():
    return template('login')

@route('/login',  method='POST')
def login():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posted_dict =  request.forms.dict
        data = json.dumps(posted_dict)
        if authenticate(posted_dict):
            auth_flag = 1
            return template('index')
        else:
            data = "1"
            resp = HTTPResponse(body=data,status=200)
            return resp

def authenticate(login_dict):
    username = posted_dict["username"][0]
    password =  posted_dict["password"][0]
    
    return True

run(host='0.0.0.0', port=8000)
