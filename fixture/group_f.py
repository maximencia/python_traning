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


    def select_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # Select first group
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.select_first_group()
        #submit
        wd.find_element_by_name("delete").click()

    def modify_first_group(self,Group):
        wd = self.app.wd
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(Group)
        wd.find_element_by_name("update").click()
        time.sleep(2)

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        # посчитаем количество чекпоксов на форме
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_group_page()
        # в консоли браузера можно набрать $$("span.group"); на странице со списком групп
        group=[]
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            group.append(Group(name=text , id=id))
        return group














