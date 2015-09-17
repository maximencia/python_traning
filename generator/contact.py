# -*- coding: utf-8 -*-
import datetime
from model.contact import Contact
import random,string
import jsonpickle
import os.path
import getopt
import sys

now_time = datetime.datetime.now()

constant = [
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


try:     # n -количество генерируемых данных f - файл
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
             for i in range (n)
            ]

# путь к файлу
file = os.path.join(os.path.dirname(os.path.abspath(__file__)),".." ,f)

# откроем в режиме write
with open(file , "w") as out:
    # сначала используем функцию для преобразования данных вначале а потом json.dump
    jsonpickle.set_encoder_options("json",indent=2)
    out.write(jsonpickle.encode(testdata))
