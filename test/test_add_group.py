# -*- coding: utf-8 -*-
import datetime
from model.group import Group

now_time = datetime.datetime.now()

def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="123_" + str(now_time),header= "123_" + str(now_time),footer= "123"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="",header="",footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
