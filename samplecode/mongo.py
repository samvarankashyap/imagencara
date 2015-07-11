import pymongo
from pymongo import MongoClient
import base64
import md5
from datetime import datetime
client = MongoClient()
db = client['test']
con = pymongo.MongoClient()
import pdb
pdb.set_trace()
user_coll = con.test.user
post_coll = con.test.posts
def initialise():
    db.create_collection("user")
    db.create_collection("posts")

def insert_user(username,password):
    password_hash = str(md5.new(password).hexdigest())
    output =user_coll.save({"username":username,"password":password_hash})
    return output

def insert_image(imagedata):
    with open('9cde01aa-b1f1-4190-a563-98151a70af27.png', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    print encoded_string
    output =user_coll.save({"image":encoded_string})
    print output
    return "inserted"

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
        print output
    else: 
        print "Record already exists"
    print record

def is_authentic(username,password):
    record = user_coll.find_one({"username": username})
    if record != None:
        password_hash = str(md5.new(password).hexdigest())
        if password_hash == record["password"]:
            return True
    return False

def get_posts_by_username(username):
    for post in post_coll.find({"username":username}):
        print post

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
    for post in post_coll.find():
        print post


register_username("samvaran2best@gmail.com","hello123")
register_username("samvarank@gmail.com","hello123")
print is_authentic("samvaran2best@gmail.com","hello123")
print is_authentic("samvarank@gmail.com","hello")
print insert_post("samvaran2best@gmail.com",22,"something")
print comment_post("samvaran2best@gmail.com",22,"somecomment")
print get_all_posts("samvaran2best@gmail.com")
print get_posts_by_username("samvaran2best@gmail.com")
#print delete_post("samvaran2best@gmail.com",22)


#insert_image("nothing")
#initialise()

