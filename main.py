from bottle import route, run, template
from bottle import route, request, response, template, HTTPResponse
import uuid
from bottle import static_file
import csv
import random
import json
import pymongo
from pymongo import MongoClient
import base64
import md5
import uuid
import os
from datetime import datetime
client = MongoClient()
db = client['test']
con = pymongo.MongoClient()
import pdb
user_coll = con.test.user
post_coll = con.test.posts

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
        if authenticate(posted_dict):
            auth_flag = 1
            data = "User authentication sucessfull"
        else:
            data = "Invalid username/password"
        resp = HTTPResponse(body=data,status=200)
        return resp

@route('/uploadimage',  method='POST')
def uploadimage():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        upload_file = request.files.get('uploadimage')
        file_name = upload_file.filename
        try:
            upload_file.save(".")
        except Exception as e:
            pass
        image_data = open(file_name,"rb").read()
        os.remove(file_name)
        user_name = request.forms.get("username")
        post_id = str(uuid.uuid1())
        output = insert_post(user_name,post_id,image_data)
        output = str(output)
        #posted_dict =  request.forms.dict
        #data = "Invalid username/password"
        resp = HTTPResponse(body=output,status=200)
        return resp

@route('/getmypictures',  method='POST')
def getmypictures():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posted_dict =  request.forms.dict
        username = posted_dict["username"][0]
        posts = get_posts_by_username(username)
        #print posts
        html_string = ""
        for post in posts:
            img1 = post['image_data']
            decode=img1.decode()
            img_tag = '<img alt="sample" src="data:image/jpeg;base64,{0}">'.format(decode)
            post_id = "'"+post['post_id']+"'"
            button_tag = "<button onclick=\"deleteimage("+post_id+")\" class='btn'>Delete Image</button>"
            html_string += img_tag+"<br>"+button_tag+"<br>"
        resp = HTTPResponse(body=html_string,status0=200)
        return resp


@route('/getallpictures',  method='POST')
def getallpictures():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posted_dict =  request.forms.dict
        username = posted_dict["username"][0]
        posts = get_all_posts(username)
        #print posts
        html_string = ""
        for post in posts:
            img1 = post['image_data']
            decode=img1.decode()
            img_tag = '<img alt="sample" src="data:image/jpeg;base64,{0}">'.format(decode)
            post_id = "'"+post['post_id']+"'"
            html_string += img_tag+"<br>"
        resp = HTTPResponse(body=html_string,status0=200)
        return resp

@route('/main')
def index():
    return template('index')


@route('/registeruser',  method='POST')
def registeruser():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posted_dict =  request.forms.dict
        username = posted_dict["username"][0]
        password =  posted_dict["password"][0]
        if register_username(username,password)!=False:
             data = "Registration successfull"
        else:
             data = "User already exists"
        resp = HTTPResponse(body=data,status=200)
        return resp


@route('/deleteimage',  method='POST')
def deletepost():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posted_dict =  request.forms.dict
        user_name = posted_dict["username"][0]
        post_id = posted_dict["post_id"][0]
        output = delete_post(user_name,post_id)
        data = str(output)
        resp = HTTPResponse(body=data,status=200)
        return resp

def authenticate(posted_dict):
    username = posted_dict["username"][0]
    password =  posted_dict["password"][0]
    if is_authentic(username,password):
        return True
    return False

def initialise():
    db.create_collection("user")
    db.create_collection("posts")

def insert_user(username,password):
    password_hash = str(md5.new(password).hexdigest())
    output =user_coll.save({"username":username,"password":password_hash})
    return output

def retrieve_image(request):
    data = db.database_name.find()
    data1 = json.loads(dumps(data))
    img = data1[0]
    img1 = img['image']
    decode=img1.decode()
    img_tag = '<img alt="sample" src="data:image/png;base64,{0}">'.format(decode)
    return HttpResponse(img_tag)

def register_username(username,password):
    record = user_coll.find_one({"username": username})
    if record == None:
        output = insert_user(username,password)
        return output
    else: 
        return False

def is_authentic(username,password):
    record = user_coll.find_one({"username": username})
    if record != None:
        password_hash = str(md5.new(password).hexdigest())
        if password_hash == record["password"]:
            return True
    return False

def get_posts_by_username(username):
    posts = []
    for post in post_coll.find({"username":username}):
        #print post
        posts.append(post)
    return posts

def insert_post(username,post_id,image_data):
    post_dict = {}
    post_dict['username']=username
    post_dict['post_id']=post_id
    encoded_string = base64.b64encode(image_data)
    post_dict['image_data']=encoded_string
    post_dict['post_time']=str(datetime.now())
    post_dict['comments']=[]
    output = post_coll.save(post_dict)
    return output

def delete_post(username,post_id):
    delete_post_dict = {}
    delete_post_dict["username"]=username
    delete_post_dict["post_id"]=post_id
    output = post_coll.remove(delete_post_dict)
    return output

def comment_post(username,post_id,comment):
    #Fetch our updated document
    given_dic = post_coll.find_one({"post_id":post_id})
    comment_dic = {}
    comment_dic["comment"]=comment 
    comment_dic["username"]=username
    comment_dic["comment_time"]=str(datetime.now())
    given_dic['comments'].append(comment_dic)
    output = post_coll.update({"post_id":post_id},given_dic)
    return output

def get_all_posts(username):
    posts = []
    for post in post_coll.find():
        posts.append(post)
    return posts

run(host='0.0.0.0', port=8000)
