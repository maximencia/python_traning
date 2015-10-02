# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_add_new_contact_in_group(app,db,data_contact,check_ui):
#def test_add_new_contact_in_group(app,db,json_contact,check_ui):
    contact=data_contact
    #contact=json_contact
    old_contacts = db.get_contacts_list()
    #надо получить имя группы
    groups = db.get_group_list()
    while True:                       # типо репеат антил
        index=randrange(len(groups)) # имя будет таким old_groups[index].name
        if len(groups[index].name)> 0:
            break
    # для дальнейшего сравнения запомним список контактов для группы из бд
    old_get_contact_in_group=db.get_contact_in_group(groups[index].name)
    #[TEST]
    app.contact.create_in_group(contact,groups[index].name)
    new_get_contact_in_group=db.get_contact_in_group(groups[index].name)
    assert len(old_get_contact_in_group) + 1  == len(new_get_contact_in_group) # хеш функция - считает количество элементов
    old_get_contact_in_group.append(contact)
    o=sorted(old_get_contact_in_group,key=Contact.id_or_max)
    n=sorted(new_get_contact_in_group,key=Contact.id_or_max)
    assert o  ==  n

    if check_ui:
        get_contact_in_group=app.contact.get_contact_in_group(groups[index].name)
        assert n  ==  sorted(app.contact.get_contacts_list(),key=Contact.id_or_max)
    # проверка для  групп

def test_add_new_contact_in_group_web(app,db,data_contact,check_ui="True"):
    i=0
    while i <= app.group.count():
        test_add_new_contact_in_group(app,db,data_contact,check_ui)
        i =i+1



def test_assert_contact_in_group_with_db(app,db):
    #получим все контакты входящие в группу из базы данных
    get_contact_in_group=db.get_contact_in_group(group_name='1')
    # получим все контакты входящие в группу на web выбрав фильтр на странице home
    get_contact_in_group=app.contact.get_contact_in_group(group_name='1')
    db= sorted(get_contact_in_group,key=Contact.id_or_max)
    web=sorted(get_contact_in_group,key=Contact.id_or_max)
    assert web == db


