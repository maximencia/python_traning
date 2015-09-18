# -*- coding: utf-8 -*-
from model.group import Group
import random
from random import randrange

def test_delete_some_group(app,db,check_ui):
      if len(db.get_group_list()) == 0:
          app.group.create(Group(name="Group for delete"))
      old_groups = db.get_group_list()
      group=random.choice(old_groups)
      #[TEST]
      app.group.delete_group_by_id(group.id)
      new_groups = db.get_group_list()
      assert len(old_groups)-1 == len(new_groups) # хеш функция - считает количество элементов
      old_groups.remove(group)
      assert old_groups == new_groups
      if check_ui:
            assert sorted(new_groups,key=Group.id_or_max)  ==  sorted(app.group.get_group_list(),key=Group.id_or_max)


# удаление всех групп != 0:  или оставляем 3 группы  > 3:
# def test_del_all_group(app):
#        while app.group.count() > 3:
#              app.group.delete_group_by_index(randrange(app.group.count()))