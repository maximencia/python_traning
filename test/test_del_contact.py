# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="1",
                              middlename="2",
                              lastname="lastname_",
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
                              notes="21"))

    old_contacts = app.contact.get_contacts_list()
    index=randrange(len(old_contacts)) # добавляем случайный выбор номера сонтакта
    #[TEST]
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1  == app.contact.count() # хеш функция - считает количество элементов
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert old_contacts ==  new_contacts

