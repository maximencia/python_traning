# -*- coding: utf-8 -*-
import mysql.connector
from fixture.orm import ORMFixture

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

