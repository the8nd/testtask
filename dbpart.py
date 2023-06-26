from pyArango.connection import *
from information import username, password

conn = Connection(username=username, password=password)
db = conn.createDatabase(name="userinfo")
db = conn["userinfo"]
userslinksCollection = db.createCollection(name="UsersLinks")


def new_user(user, link):
    doc = userslinksCollection.createDocument()
    doc['login'] = user
    doc['links'] = [link]
    doc._key = ''.join(user).lower()
    doc.save()


def link_addder(user, link):
    doc = userslinksCollection[user]
    doc['links'] = doc['links'].append(link)
    doc.save()
