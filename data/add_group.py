# -*- coding: utf-8 -*-
import datetime
from model.group import Group
import random,string

now_time = datetime.datetime.now()

constant = [
            Group(name="1",header="2",footer= "3"),
            Group(name="4",header="5",footer= "6")
        ]


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits# + " "*10 #добавим 10 пробелов + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [Group(name="",header="",footer= "")]+[
            Group(name=random_string("name" , 10),header=random_string("header" , 10),footer=random_string("footer" , 10))
            for i in range (5)
            ]
# 8 вариантов
#testdata = [ Group(name=name,header=header,footer=footer) for name in ["",random_string("name" , 10)] for header in ["",random_string("header" , 10)] for footer in ["",random_string("footer" , 10)] ]
