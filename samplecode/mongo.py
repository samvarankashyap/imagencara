import pymongo
from pymongo import MongoClient
import base64
import md5
client = MongoClient()
db = client['test']
con = pymongo.MongoClient()
import pdb
pdb.set_trace()
user_coll = con.test.user

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

register_username("samvaran2best@gmail.com","hello123")
register_username("samvarank@gmail.com","hello123")
print is_authentic("samvaran2best@gmail.com","hello123")
print is_authentic("samvarank@gmail.com","hello")

#insert_image("nothing")
#initialise()

