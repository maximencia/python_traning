# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact
from random import randrange
import random
import time

now_time = datetime.datetime.now()

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="for modifdy"))
    old_contacts = app.contact.get_contacts_list()
    contact=Contact(firstname="1+m",
                                              middlename="2+m",
                                              lastname=("modify_lastname_"),
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
                                              phone2="20"#,
                                             # notes="21+m"
                                             )
    index=randrange(len(old_contacts))
    contact .id = old_contacts[index].id
    #[TEST]
    app.contact.modify_contact_by_index(contact,index)
    assert len(old_contacts)  == app.contact.count() # хеш функция - считает количество элементов
    new_contacts = app.contact.get_contacts_list()
    # список обновим до модифицированных значений и сравним оба списка
    old_contacts[index]= contact
    assert sorted(old_contacts,key=Contact.id_or_max)  ==  sorted(new_contacts,key=Contact.id_or_max)


def test_modify_contact_db_assert(app,db,check_ui):
    mm = str(random.randint(100, 999)) # 3 цифры из даты , достаточно случайные
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="for modify test_"+mm))
    contact=Contact(firstname="firstname_"+mm,
                    middlename="middlename_"+mm,
                    lastname=("lastname_"+mm))
    old_contacts = db.get_contacts_list()
    index=randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    id= contact.id
    #[TEST]
    app.contact.modify_contact_by_id(contact,id)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts)  == len(new_contacts) # хеш функция - считает количество элементов
    # список обновим до модифицированных значений и сравним оба списка
    old_contacts[index]= contact
    o = old_contacts
    n = new_contacts
    assert sorted(o,key=Contact.id_or_max)  ==  sorted(n,key=Contact.id_or_max)
    if check_ui:
        assert sorted(n,key=Contact.id_or_max)  ==  sorted(app.contact.get_contacts_list(),key=Contact.id_or_max)

def test_modify_some_contacts(app,db,check_ui="True"):
    i=0
    while i <= app.contact.count():
        test_modify_contact_db_assert(app,db,check_ui)
        i =i+1


