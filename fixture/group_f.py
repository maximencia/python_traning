# -*- coding: utf-8 -*-
__author__ = 'Maxim.Rumyantsev'

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

    def create(self,Group):
        wd = self.app.wd
        self.open_group_page()
        # fill group form
        wd.find_element_by_name("new").click()
        self.app.fill_text_field(name="group_name",send_keys_parameters=Group.name)
        self.app.fill_text_field(name="group_header",send_keys_parameters=Group.header)
        self.app.fill_text_field(name="group_footer",send_keys_parameters=Group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to group page
        self.return_to_group_page()
