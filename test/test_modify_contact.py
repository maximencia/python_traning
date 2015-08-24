# -*- coding: utf-8 -*-
import datetime
from model.group import Contact

now_time = datetime.datetime.now()

def test_modify_first_group(app):
    app.session.login(username="admin",password="secret")
    app.contact.modify_first_contact(Contact(firstname="1+m",
                                              middlename="2+m",
                                              lastname=("modify_lastname_" + str(now_time)),
                                              nickname="4+m",
                                              title="6",
                                              company="7",
                                              address="8",
                                              home="9",
                                              mobile="10",
                                              work="11",
                                              fax="12",
                                              email2="14",
                                              email3="15",
                                              homepage="16",
                                              address2="19",
                                              phone2="20",
                                              notes="21+m"))
    app.session.logout()


