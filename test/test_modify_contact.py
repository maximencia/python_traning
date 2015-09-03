# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact
now_time = datetime.datetime.now()

def test_modify_first_group(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="for modifdy"))
    old_contacts = app.contact.get_contacts_list()
    contact=Contact(firstname="1+m",
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
                                              phone2="20"#,
                                             # notes="21+m"
                                             )
    contact.id = old_contacts[0].id
    #[TEST]
    app.contact.modify_first_contact(contact)
    assert len(old_contacts)  == app.contact.count() # хеш функция - считает количество элементов
    new_contacts = app.contact.get_contacts_list()
    # список обновим до модифицированных значений и сравним оба списка
    old_contacts[0]= contact
    assert sorted(old_contacts,key=Contact.id_or_max)  ==  sorted(new_contacts,key=Contact.id_or_max)



