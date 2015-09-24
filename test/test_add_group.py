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

# для проверки загружаем данные из DB напрямую.
def test_add_group_with_db_load(app, db, json_groups):
    group = json_groups #загружаем данные из файла C:\python_traning\python_traning\data\groups.py но через conftest
    old_groups = db.get_group_list()
    #[TEST]
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count() # хеш функция - считает количество элементов , но при работе с bd такое хеширование выполняется долго и мы можем от него отказаться
    new_groups = db.get_group_list()
    old_groups.append(group)
    old=sorted(old_groups,key=Group.id_or_max)
    new=sorted(new_groups,key=Group.id_or_max)
    assert old == new
