from bottle import route, run, template
from bottle import route, request, response, template, HTTPResponse

import uuid
from bottle import static_file
import csv
import random
import json


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="static")

@route('/')
def index():
    return template('login')

@route('/login',  method='POST')
def clusterimage():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posted_dict =  request.forms.dict
        data = json.dumps(posted_dict)
        resp = HTTPResponse(body=data,status=200)
        return resp
    else:
        return 'This is a normal request'

run(host='0.0.0.0', port=8000)
