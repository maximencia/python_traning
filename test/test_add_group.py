# -*- coding: utf-8 -*-
import datetime
from model.group import Group

now_time = datetime.datetime.now()

def test_add_group(app):
    app.session.login(username="admin",password="secret")
    app.group.create(Group(name="123_" + str(now_time),header= "123_" + str(now_time),footer= "123"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin",password="secret")
    app.group.create(Group(name="",header= "",footer= ""))
    app.session.logout()

