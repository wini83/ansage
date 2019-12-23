# -*- coding: utf-8 -*-
'''
Created on 16 wrz 2018

@author: Mariusz Wincior
'''


from flask import *
from peewee import *
import datetime


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
    is_admin = BooleanField()    


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
    is_ready = BooleanField()
    
# simple utility function to create tables
def create_tables():
    with database:
        database.create_tables([User, Announce])
        


def install():
    create_tables()
    database.connect()
    with database.atomic():
        User.create(username='admin', password="qwerty", email="admin@server.com", join_date=datetime.date(2018,1,1), enabled = True, is_admin = True)
        User.create(username='user1', password="qwerty", email="user1@server.com", join_date=datetime.date(2018,1,1), enabled = False, is_admin = False)   
        User.create(username='user2', password="qwerty", email="user2@server.com", join_date=datetime.date(2018,1,1), enabled = False, is_admin = False)
    database.close()

def createsampleAnn():
    database.connect()
    admin = User.select().where(User.username == "admin").get()
    Announce.create(user = admin, text = "Pociąg specjalny przejedzie przez tor przy peronie drugim", aired = False, is_downloaded = False, is_from_TTS = True, is_private = False, add_date = datetime.datetime.now(), air_date = datetime.datetime.now(), filename = "", is_ready = False)
 
#install()
createsampleAnn()




    
