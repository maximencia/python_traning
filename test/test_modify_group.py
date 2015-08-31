# -*- coding: utf-8 -*-
import datetime
from model.group import Group

now_time = datetime.datetime.now()

def test_modify_first_group(app):
    # если не существует ни одной группы - создаем
    if app.group.count() == 0:
         app.group.create(Group(name="Group for delete"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="modify_123_" + str(now_time),footer="Modify"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)