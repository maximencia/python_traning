# -*- coding: utf-8 -*-
import datetime
from model.group import Group
from sys import maxsize

now_time = datetime.datetime.now()

def test_add_group(app):
    old_groups = app.group.get_group_list()
    #с таким именнем тест для 4_3 падает group=Group(name="123_" + str(now_time),header= "123_" + str(now_time),footer= "123")
    #group=Group(name="",header= "",footer= "")
    group=Group(name="name",header= "123_" + str(now_time),footer= "123")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group=Group(name="1",header="1",footer="1")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)