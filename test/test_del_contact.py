# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_delete_random_contact(app):
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

def test_delete_random_contact_db_assert(app,db,check_ui):
    if len(db.get_contacts_list()) == 0:
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

    old_contacts = db.get_contacts_list()
    old=db.get_contacts_list()
    index=randrange(len(old_contacts)) # случайный выбор номера сонтакта, но нам обязательно нужно получитьь ID контакта
    id= old_contacts[index].id
    #[TEST]
    app.contact.delete_contact_by_id(id)
    assert len(old_contacts) - 1  == len(db.get_contacts_list()) # хеш функция - считает количество элементов
    new_contacts = db.get_contacts_list()
    old_contacts[index:index+1] = [] #а я пожалуй оставлю так , подожду когда упадет но лучше использовать old_contacts.remove(group)
    n= new_contacts
    o = old_contacts
    assert o == n
    #if check_ui:
    assert sorted(new_contacts,key=Contact.id_or_max)  ==  sorted(app.contact.get_contacts_list(),key=Contact.id_or_max)

# удаление всех
def test_del_all_contact(app,db):
        while app.contact.count() > 0:
              #app.group.delete_group_by_index(randrange(app.group.count()))
              test_delete_random_contact_db_assert(app,db,check_ui="True")
