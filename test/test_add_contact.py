# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact
import random,pytest,string

now_time = datetime.datetime.now()

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits# + " "*10 #добавим 10 пробелов + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_phone(prefix,maxlen):
    symbols = string.digits + "(" + ")" + "-"
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_email(prefix,maxlen):
    symbols =  string.ascii_letters + string.digits
    domen=string.ascii_lowercase #Константное перечисление букв из набора ASCII в нижнем регистре.
    return prefix + ("".join([random.choice(symbols) for i in range (random.randrange(maxlen//2))]))+"@"+\
           ("".join([random.choice(symbols) for i in range (random.randrange(maxlen//2))]))+"."+\
            ("".join([random.choice(domen) for i in range (random.randint(2, 3))])) # Return a random integer N such that a <= N <= b.

testdata = [Contact(firstname=random_string("firstname" , 10),
                     middlename=random_string("middlename" , 10),
                     lastname=random_string("lastname" , 10),
                     nickname=random_string("nickname" , 10),
                     title=random_string("firstname" , 10),
                     company=random_string("firstname" , 10),
                     address=random_string("firstname" , 10),
                     home=random_phone("" , 10),
                     mobile=random_phone("" , 10),
                     work=random_phone("" , 10),
                     fax=random_phone("" , 10),
                     email2=random_email("email2" , 15),
                     email3=random_email("email3" , 15),
                     homepage=random_string("homepage" , 10),
                     address2=random_string("address2" , 10),
                     phone2=random_phone("" , 10),
                     notes=random_string("notes" , 10))
             for i in range (5)
            ]


@pytest.mark.parametrize("group_param",testdata,ids=[repr(x) for x in testdata])
def test_add_contact(app,group_param):
    old_contacts = app.contact.get_contacts_list()
    #[TEST]
    app.contact.create(group_param)
    assert len(old_contacts) + 1  == app.contact.count() # хеш функция - считает количество элементов
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(group_param)
    o=sorted(old_contacts,key=Contact.id_or_max)
    n=sorted(new_contacts,key=Contact.id_or_max)
    assert sorted(old_contacts,key=Contact.id_or_max)  ==  sorted(new_contacts,key=Contact.id_or_max)

