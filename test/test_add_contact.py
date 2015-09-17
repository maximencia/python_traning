# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app,data_contact):
    contact=data_contact
    old_contacts = app.contact.get_contacts_list()
    #[TEST]
    app.contact.create(contact)
    assert len(old_contacts) + 1  == app.contact.count() # хеш функция - считает количество элементов
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    o=sorted(old_contacts,key=Contact.id_or_max)
    n=sorted(new_contacts,key=Contact.id_or_max)
    assert sorted(old_contacts,key=Contact.id_or_max)  ==  sorted(new_contacts,key=Contact.id_or_max)

