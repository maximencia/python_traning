# -*- coding: utf-8 -*-
import datetime
from model.group import Group

now_time = datetime.datetime.now()

def test_modify_first_group(app):
    app.session.login(username="admin",password="secret")
    app.group.modify_first_group(Group(name="modify_123_" + str(now_time),header= "123_" + str(now_time),footer= "Modify_123"))
    app.session.logout()


