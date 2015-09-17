# -*- coding: utf-8 -*-
from model.group import Group




def test_add_group(app, data_groups):
    group = data_groups #загружаем данные из файла C:\python_traning\python_traning\data\groups.py но через conftest
    old_groups = app.group.get_group_list()
    #[TEST]
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count() # хеш функция - считает количество элементов
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    o=sorted(old_groups,key=Group.id_or_max)
    t=sorted(new_groups,key=Group.id_or_max)
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)
    p=1