# -*- coding: utf-8 -*-
import datetime
from model.group import Group
import pytest,random,string


now_time = datetime.datetime.now()

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits# + " "*10 #добавим 10 пробелов + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [Group(name="",header="",footer= "")]+[
            Group(name=random_string("name" , 10),header=random_string("header" , 10),footer=random_string("footer" , 10))
            for i in range (5)
            ]
# 8 вариантов
#testdata = [ Group(name=name,header=header,footer=footer) for name in ["",random_string("name" , 10)] for header in ["",random_string("header" , 10)] for footer in ["",random_string("footer" , 10)] ]

@pytest.mark.parametrize("group_param",testdata,ids=[repr(x) for x in testdata])
def test_add_group(app,group_param):
    old_groups = app.group.get_group_list()
    #[TEST]
    app.group.create(group_param)
    assert len(old_groups) + 1 == app.group.count() # хеш функция - считает количество элементов
    new_groups = app.group.get_group_list()
    old_groups.append(group_param)
    o=sorted(old_groups,key=Group.id_or_max)
    t=sorted(new_groups,key=Group.id_or_max)
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)
    p=1