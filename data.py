'''
Created on 16 wrz 2018

@author: Mariusz Wincior
'''

from flask import *
from peewee import *
from datetime import date


# config - aside from our database, the rest is for use by Flask
DATABASE = 'ansage.db'
DEBUG = True


database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database

# the user model specifies its fields (or columns) declaratively, like django
class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()
    enabled = BooleanField()    


class Announce(BaseModel):
    user = ForeignKeyField(User, backref='messages')
    text = TextField()
    aired = BooleanField()
    is_downloaded = BooleanField()
    is_from_TTS = BooleanField()
    is_private = BooleanField()
    add_date = DateTimeField()
    air_date = DateTimeField()
    filename = CharField()
    
# simple utility function to create tables
def create_tables():
    with database:
        database.create_tables([User, Announce])
        
        

#create_tables()

# database.connect()
# with database.atomic():
#     user1 = User.create(username='user2', password="qwerty", email="user2@server.com", join_date=date(2018,1,1), enabled = False)
# database.close()
        
