# -*- coding: utf-8 -*-
import datetime
now_time = datetime.datetime.now()

def test_delete_first_group(app):
    app.session.login(username="admin",password="secret")
    app.group.delete_first_group()
    app.session.logout()

