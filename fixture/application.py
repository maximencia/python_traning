# -*- coding: utf-8 -*-
__author__ = 'Maxim.Rumyantsev'
from selenium.webdriver.firefox.webdriver import WebDriver
import datetime
from model.group import add_contact_form
from fixture.session_f import SessionHelper
from fixture.group_f import GroupHelper



class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

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

    def hello(s):
        """

        :rtype : obnamet
        """
        print('Hi')


    def form_add_contact_group4(self, add_contact_group4):
        wd = self.wd
        # SECONDARY
        Application.fill_text_field(self,name="address2",send_keys_parameters=add_contact_group4.address2)
        Application.fill_text_field(self,name="phone2",send_keys_parameters=add_contact_group4.phone2)
        Application.fill_text_field(self,name="notes",send_keys_parameters=add_contact_group4.notes)

    def form_add_contact_group3(self):
        wd = self.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        Application.fill_text_field(self,name="byear",send_keys_parameters="2017")

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[18]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[18]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()
        Application.fill_text_field(self,name="ayear",send_keys_parameters="2018")
        #выбор  имени группы

    def form_add_contact_group2(self,add_contact_group2):
        wd = self.wd
        # telephon & emails
        Application.fill_text_field(self,name="home",send_keys_parameters=add_contact_group2.home)
        Application.fill_text_field(self,name="mobile",send_keys_parameters=add_contact_group2.mobile)
        Application.fill_text_field(self,name="work",send_keys_parameters=add_contact_group2.work)
        Application.fill_text_field(self,name="fax",send_keys_parameters=add_contact_group2.fax)
        # email # 1 заполняется автоматически
        #Application.fill_text_field(self,name="email1",send_keys_parameters=add_contact_group2.email1)
        Application.fill_text_field(self,name="email2",send_keys_parameters=add_contact_group2.email2)
        Application.fill_text_field(self,name="email3",send_keys_parameters=add_contact_group2.email3)
        Application.fill_text_field(self,name="homepage",send_keys_parameters=add_contact_group2.homepage)

    def form_add_contact_group1(self,add_contact_group1):
        wd = self.wd
        # CONTACT_INFO
        Application.fill_text_field(self,name="firstname",send_keys_parameters=add_contact_group1.firstname)
        Application.fill_text_field(self,name="middlename",send_keys_parameters=add_contact_group1.middlename)
        Application.fill_text_field(self,name="lastname",send_keys_parameters=add_contact_group1.lastname)
        Application.fill_text_field(self,name="nickname",send_keys_parameters=add_contact_group1.nickname)
        # пропущено добавление фото
        Application.fill_text_field(self,name="title",send_keys_parameters=add_contact_group1.title)
        Application.fill_text_field(self,name="company",send_keys_parameters=add_contact_group1.company)
        Application.fill_text_field(self,name="address",send_keys_parameters=add_contact_group1.address)

    #Объеденим группы в одном методе
    def fill_add_contact_form(self,
                              group_1=add_contact_form.add_contact_group1,
                              group_2=add_contact_form.add_contact_group2,
                              group_4=add_contact_form.add_contact_group4):
        wd = self.wd
        self.open_new_contact_form()
        self.form_add_contact_group1(group_1)
        self.form_add_contact_group2(group_2)
        self.form_add_contact_group3()
        self.form_add_contact_group4(group_4)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_new_contact_form(self):
        wd = self.wd
        # add_new_contact_form
        wd.find_element_by_link_text("add new").click()

    def destroy(self):
        self.wd.quit()




