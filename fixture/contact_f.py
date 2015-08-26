# -*- coding: utf-8 -*-
__author__ = 'Maxim.Rumyantsev'

class ContactHelper:

    def __init__(self,app):
        self.app=app

    def open_new_contact_form(self):
        wd = self.app.wd
        # add_new_contact_form
        wd.find_element_by_link_text("add new").click()

    def open_home_form(self):
        wd = self.app.wd
        # add_new_contact_form
        wd.find_element_by_link_text("home").click()

    def fill_contact_form(self,Contact):
        wd = self.app.wd
        # CONTACT_INFO
        self.app.fill_text_field(name="firstname",send_keys_parameters=Contact.firstname)
        self.app.fill_text_field(name="middlename",send_keys_parameters=Contact.middlename)
        self.app.fill_text_field(name="lastname",send_keys_parameters=Contact.lastname)
        self.app.fill_text_field(name="nickname",send_keys_parameters=Contact.nickname)
        # пропущено добавление фото
        self.app.fill_text_field(name="title",send_keys_parameters=Contact.title)
        self.app.fill_text_field(name="company",send_keys_parameters=Contact.company)
        self.app.fill_text_field(name="address",send_keys_parameters=Contact.address)
        # telephon & emails
        self.app.fill_text_field(name="home",send_keys_parameters=Contact.home)
        self.app.fill_text_field(name="mobile",send_keys_parameters=Contact.mobile)
        self.app.fill_text_field(name="work",send_keys_parameters=Contact.work)
        self.app.fill_text_field(name="fax",send_keys_parameters=Contact.fax)
        # email # 1 заполняется автоматически
        #self.app.fill_text_field(name="email1",send_keys_parameters=Contact.email1)
        self.app.fill_text_field(name="email2",send_keys_parameters=Contact.email2)
        self.app.fill_text_field(name="email3",send_keys_parameters=Contact.email3)
        self.app.fill_text_field(name="homepage",send_keys_parameters=Contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        self.app.fill_text_field(name="byear",send_keys_parameters="2017")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[18]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[18]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()
        self.app.fill_text_field(name="ayear",send_keys_parameters="2018")
        #выбор  имени группы
        # SECONDARY
        self.app.fill_text_field(name="address2",send_keys_parameters=Contact.address2)
        self.app.fill_text_field(name="phone2",send_keys_parameters=Contact.phone2)
        self.app.fill_text_field(name="notes",send_keys_parameters=Contact.notes)


    def create(self,Contact):
        wd = self.app.wd
        self.open_new_contact_form()
        self.fill_contact_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def modify_first_contact(self,Contact):
        wd = self.app.wd
        self.open_home_form()
        #нужно обязательно выбрать контакт
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_form(Contact)
        #update submit
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_form()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        self.open_home_form()
        # посчитаем количество чекпоксов на форме
        return len(wd.find_elements_by_name("selected[]"))


