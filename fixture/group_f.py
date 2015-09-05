# -*- coding: utf-8 -*-
__author__ = 'Maxim.Rumyantsev'
import time
from model.group import Group

class GroupHelper:

    def __init__(self,app):
        self.app=app

    def open_group_page(self):
        wd = self.app.wd
        # добавим проверку - если адрес страницы заканчивается на /group.php и на странице есть кноgка "создать группу:" тогда переходить не нужно
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()

    def fill_group_form(self,Group):
        self.app.fill_text_field(name="group_name",send_keys_parameters=Group.name)
        self.app.fill_text_field(name="group_header",send_keys_parameters=Group.header)
        self.app.fill_text_field(name="group_footer",send_keys_parameters=Group.footer)

    def create(self,Group):
        wd = self.app.wd
        self.open_group_page()
        # fill group form
        wd.find_element_by_name("new").click()
        self.fill_group_form(Group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # после добавления кешь становится не валидным - мы должны его сбросить
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        self.select_group_by_index(index=0)

    def select_group_by_index(self,index):
        wd = self.app.wd
        self.open_group_page()
        # Select first group
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_group(self):
        wd = self.app.wd
        self.delete_group_by_index(index=0)

    def delete_group_by_index(self,index):
        wd = self.app.wd
        self.select_group_by_index(index)
        #submit
        wd.find_element_by_name("delete").click()
        # после кешь становится не валидным - мы должны его сбросить
        self.group_cache = None

    def modify_first_group(self,Group):
        wd = self.app.wd
        self.modify_group_by_index(index=0)

    def modify_group_by_index(self,Group,index):
        wd = self.app.wd
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(Group)
        wd.find_element_by_name("update").click()
        # после кешь становится не валидным - мы должны его сбросить
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        # посчитаем количество чекпоксов на форме
        return len(wd.find_elements_by_name("selected[]"))


    # Добавлено кеширование, и оно не должно работать после добавления изменения и удаления группы self.group_cache = None
    group_cache = None
    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            # в консоли браузера можно набрать $$("span.group"); на странице со списком групп
            self.group_cache=[]
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text , id=id))
        return list(self.group_cache)














