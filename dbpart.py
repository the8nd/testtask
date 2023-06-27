from pyArango.connection import *
from information import username, password

conn = Connection(username=username, password=password)
#db = conn.createDatabase(name="userinfo")
db = conn["userinfo"]
#usersfilesCollection = db.createCollection(name="UsersFiles")
usersfilesCollection = db.collections["UsersFiles"]


def new_user(user, link):
    doc = usersfilesCollection.createDocument()
    doc['login'] = user
    doc['files'] = [link]
    doc._key = ''.join(user).lower()
    doc.save()
    print(doc)


def link_addder(user, link):
    doc = usersfilesCollection[user]
    c = list(doc['files'])
    c.append(link)
    doc['files'] = c
    doc.save()
