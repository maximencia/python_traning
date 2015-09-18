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

# def test_group_list_2(app, db):
#     print(timeit(lambda: app.group.get_group_list(), number=1))
#     def clean(group):
#         return Group(id=group.id, name=group.name.strip())
#     print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
#     assert False #sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
#
#     ..\..\..\..\..\..\python_traning\python_traning\test\test_db_match_ui.py 0.323984470927
# 0.565849749605