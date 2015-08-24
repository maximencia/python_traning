# -*- coding: utf-8 -*-
__author__ = 'Maxim.Rumyantsev'
import time

class GroupHelper:

    def __init__(self,app):
        self.app=app

    def open_group_page(self):
        # init group creation
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        # return to group page
        wd.find_element_by_link_text("group page").click()

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
        # return to group page
        self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        #Select first group
        wd.find_element_by_name("selected[]").click()
        #submit
        wd.find_element_by_name("delete").click()

    def modify_first_group(self,Group):
        wd = self.app.wd
        self.open_group_page()
        #нужно обязательно выбрать что-то
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(Group)
        wd.find_element_by_name("update").click()
        time.sleep(2)






