# -*- coding: utf-8 -*-
#from data.add_group import testdata
from data.add_group import constant as testdata
from model.group import Group
import pytest



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