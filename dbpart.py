from pyArango.connection import *
from information import username, password

conn = Connection(username=username, password=password)
#db = conn.createDatabase(name="userinfo") # Для первого запуска и создания БД
db = conn["userinfo"]
#usersfilesCollection = db.createCollection(name="UsersFiles") # Для первого запуска и создания коллекции
usersfilesCollection = db.collections["UsersFiles"]


def new_user(user, link):
    doc = usersfilesCollection.createDocument()
    doc['login'] = user
    doc['files'] = [link]
    doc._key = ''.join(user).lower()
    doc.save()


def link_addder(user, link):
    doc = usersfilesCollection[user]
    c = list(doc['files'])
    c.append(link)
    doc['files'] = c
    doc.save()
