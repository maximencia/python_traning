# -*- coding: utf-8 -*-
import mysql.connector
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

db = ORMFixture(host="127.0.0.1",name="addressbook",user="root",password="")


connection = mysql.connector.connect(host="127.0.0.1",database="addressbook", user="root", password="")


try:
    l = db.get_group_list()
    for item in l:
                print(item)
finally:
    pass #db.destroy() ORM автоматически закрывает сессию с БД


try:
    l = db.get_contact_list()
    for item in l:
                print(item)
finally:
    pass #db.destroy() ORM автоматически закрывает сессию с БД


try:
    l = db.get_contacts_in_group(Group(id="804"))
    for item in l:
                print(item)
finally:
    pass #db.destroy() ORM автоматически закрывает сессию с БД

try:
    l = db.get_contacts_not_in_group(Group(id="804"))
    for item in l:
                print(item)
finally:
    pass #db.destroy() ORM автоматически закрывает сессию с БД

