# -*- coding: utf-8 -*-
from model.contact import Contact
import datetime

now_time = datetime.datetime.now()

testdata = [
            Contact(firstname="1",
                    middlename="2",
                    lastname=("lastname_" + str(now_time)),
                    nickname="4",
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
                    notes="21")
        ]