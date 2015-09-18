# -*- coding: utf-8 -*-

from model.group import Group
from timeit import timeit

def test_group_list(app, db):
    ui_list=app.group.get_group_list()
    # удалять пробелы из списка который выгрузился из bd мы будем прямо в тесте -
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list=map(clean,db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)