# -*- coding: utf-8 -*-
import datetime
from model.group import Group
from random import randrange
now_time = datetime.datetime.now()

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