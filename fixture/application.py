# -*- coding: utf-8 -*-
__author__ = 'Maxim.Rumyantsev'
from selenium.webdriver.firefox.webdriver import WebDriver
import datetime
from fixture.session_f import SessionHelper
from fixture.group_f import GroupHelper
from fixture.contact_f import ContactHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

 # заполнение  тестовых полей
    def fill_text_field(self,name,send_keys_parameters):
        wd = self.wd
        wd.find_element_by_name(name).click()
        wd.find_element_by_name(name).clear()
        wd.find_element_by_name(name).send_keys(send_keys_parameters)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def time_now(self):
        return datetime.datetime.now()

    def destroy(self):
        self.wd.quit()



