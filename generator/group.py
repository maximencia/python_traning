# -*- coding: utf-8 -*-
import datetime
from model.group import Group
import random,string
import jsonpickle
import os.path
import getopt
import sys

now_time = datetime.datetime.now()

constant = [
            Group(name="1",header="2",footer= "3"),
            Group(name="4",header="5",footer= "6")
        ]


try:     # n -количество генерируемых данных f - файл
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits# + " "*10 #добавим 10 пробелов + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [Group(name="",header="",footer= "")]+[
            Group(name=random_string("name" , 10),header=random_string("header" , 10),footer=random_string("footer" , 10))
            for i in range (n)
            ]
# 8 вариантов
#testdata = [ Group(name=name,header=header,footer=footer) for name in ["",random_string("name" , 10)] for header in ["",random_string("header" , 10)] for footer in ["",random_string("footer" , 10)] ]


# путь к файлу
file = os.path.join(os.path.dirname(os.path.abspath(__file__)),".." ,f)

# откроем в режиме write
with open(file , "w") as out:
    # сначала используем функцию для преобразования данных вначале а потом json.dump
    jsonpickle.set_encoder_options("json",indent=2)
    out.write(jsonpickle.encode(testdata))
