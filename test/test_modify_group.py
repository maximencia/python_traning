# -*- coding: utf-8 -*-
import datetime
from model.group import Group

now_time = datetime.datetime.now()

def test_modify_first_group(app):
    # если не существует ни одной группы - создаем
    if app.group.count() == 0:
         app.group.create(Group(name="Group for delete"))

    old_groups = app.group.get_group_list()
    group = Group(name="modify_123_" + str(now_time),footer="Modify")
    # запомним идендификатор изменяемой группы, а группа то у нас первая по этому [0]
    group.id = old_groups[0].id
    # сам ТЕСТ на модификацию
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    # список обновим до модифицированных значений и сравним оба списка
    old_groups[0]= group
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups , key=Group.id_or_max)
