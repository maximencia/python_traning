# -*- coding: utf-8 -*-
import datetime
from model.group import Group
from random import randrange
import random

now_time= datetime.datetime.now()

def test_modify_random_group(app):
    # если не существует ни одной группы - создаем
    if app.group.count() == 0:
         app.group.create(Group(name="Group for modify test"))
    old_groups = app.group.get_group_list()
    index=randrange(len(old_groups))
    group = Group(name="modify_123_" + str(now_time),footer="Modify")
    # запомним идендификатор изменяемой группы, а группа то у нас рандомная берем index
    group.id = old_groups[index].id
    #[ТЕСТ]
    app.group.modify_group_by_index(group,index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    # список обновим до модифицированных значений и сравним оба списка
    old_groups[index]= group
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups , key=Group.id_or_max)


# Используем базу для загрузки списков
def test_modify_random_group_2(app,db,check_ui):
    mm = str(random.randint(100, 999)) # 3 цифры из даты , достаточно случайные
    # если не существует ни одной группы - создаем
    if len(db.get_group_list()) == 0:
         app.group.create(Group(name="Group for modify test"+mm))
    old_groups = db.get_group_list()
    index=randrange(len(old_groups))
    group = Group(name="name_mod_"+mm,footer="foot_mod"+mm)
    group.id = old_groups[index].id
    #[ТЕСТ]
    app.group.modify_group_by_id(group.id ,group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups) # хеш функция - считает количество элементов
    # список обновим до модифицированных значений и сравним оба списка
    old_groups[index]= group
    o=old_groups
    n= new_groups
    assert sorted(o,key=Group.id_or_max) == sorted(n , key=Group.id_or_max)
    if check_ui:
        assert sorted(n,key=Group.id_or_max)  ==  sorted(app.group.get_group_list(),key=Group.id_or_max)

def test_modify_each_group(app,db,check_ui="True"):
    i=0
    while i <= app.group.count():
        test_modify_random_group_2(app,db,check_ui)
        i =i+1

