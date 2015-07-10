# models.py
import peewee 
database = peewee.MySQLDatabase("imagencara", host="localhost", port=3306, user="root", passwd="root")

########################################################################
class User(peewee.Model):
    """
    ORM model of the Artist table
    """
    username = peewee.CharField()
    password = peewee.CharField()
    class Meta:
        database = database
 
########################################################################
class Post(peewee.Model):
    """
    ORM model of album table
    """
    username = peewee.ForeignKeyField(User)
    image = peewee.BlobField()
    release_date = peewee.DateTimeField()
    publisher = peewee.CharField()
    media_type = peewee.CharField()
 
    class Meta:
        database = database

class PostComments(peewee.Model):
    """
    ORM model of album table
    """
    post = peewee.ForeignKeyField(Post)
    release_date = peewee.DateTimeField()
    publisher = peewee.CharField()
    media_type = peewee.CharField()

    class Meta:
        database = database
 
 
if __name__ == "__main__":
    try:
        Artist.create_table()
    except peewee.OperationalError:
        print "Artist table already exists!"
 
    try:
        Album.create_table()
    except peewee.OperationalError:
        print "Album table already exists!"
