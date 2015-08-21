# -*- coding: utf-8 -*-
import datetime
now_time = datetime.datetime.now()

def test_delete_first_contact(app):
    app.session.login(username="admin",password="secret")
    app.contact.delete_first_contact()
    app.session.logout()

