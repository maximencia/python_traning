# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import datetime, unittest
#from group import add_contact_group1,add_contact_group2,add_contact_group4
from group import add_contact_form

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

now_time = datetime.datetime.now()

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    # def test_(self):
    #     success = True

    def form_add_contact_group4(self, wd, add_contact_group4):
        # SECONDARY
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(add_contact_group4.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(add_contact_group4.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(add_contact_group4.notes)

    def form_add_contact_group3(self, wd):
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2017")

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[18]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[18]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2018")
        #выбор  имени группы

    def form_add_contact_group2(self, wd, add_contact_group2):
        # telephon & emails
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(add_contact_group2.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(add_contact_group2.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(add_contact_group2.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(add_contact_group2.fax)
        # email # 1 заполняется автоматически
        # wd.find_element_by_name("email1").click()
        # wd.find_element_by_name("email1").clear()
        # wd.find_element_by_name("email1").send_keys(add_contact_group2.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(add_contact_group2.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(add_contact_group2.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(add_contact_group2.homepage)

    def form_add_contact_group1(self, wd, add_contact_group1):
        # CONTACT_INFO
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(add_contact_group1.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(add_contact_group1.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(add_contact_group1.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(add_contact_group1.nickname)
        # пропущено добавление фото
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(add_contact_group1.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(add_contact_group1.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(add_contact_group1.address)

    def open_new_contact_form(self, wd):
        # add_new_contact_form
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, login, password):
        self.go_to_homepage(wd)
        # Login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def go_to_homepage(self, wd):
        # go to application
        wd.get("http://localhost/addressbook/")

    #Объеденим группы в одном методе
    def fill_add_contact_form(self, wd,
                              group_1=add_contact_form.add_contact_group1,
                              group_2=add_contact_form.add_contact_group2,
                              group_4=add_contact_form.add_contact_group4):
        self.open_new_contact_form(wd)
        self.form_add_contact_group1(wd, group_1)
        self.form_add_contact_group2(wd, group_2)
        self.form_add_contact_group3(wd)
        self.form_add_contact_group4(wd, group_4)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


#начало теста ###########################################################################################
    def test_test_add_contact(self):
        wd = self.wd

        self.login(wd, "admin", "secret")
      # # fill new contact form
    #     form_add_contact_
    #                      _group1  (main info)
    #                             firstname
    #                             middlename
    #                             lastname
    #                             nickname
    #                             # пропущено добавление фото
    #                             title
    #                             company
    #                             address

    #                      _group2  (telephon & emails)
    #                             home
    #                             mobile
    #                             work
    #                             fax
    #                             # email # 1 заполняется автоматически
    #                             email2
    #                             email3
    #                             homepage

    #                      _group3  (date & group)
    #                             birthday
    #                             anniversary
    #                             # должна выбираться группа group
    #                      _group4  (secondary )
    #                             address2
    #                             phone2
    #                             notes
        self.fill_add_contact_form(wd,
                                   group_1=add_contact_form.add_contact_group1(firstname="1",
                                                                                  middlename="2",
                                                                                  lastname=("lastname_" + str(now_time)),
                                                                                  nickname="4",
                                                                                  title="6",
                                                                                  company="7",
                                                                                  address="8"),
                                   group_2=add_contact_form.add_contact_group2(home="9",
                                                                               mobile="10",
                                                                               work="11",
                                                                               fax="12",
                                                                               email2="14",
                                                                               email3="15",
                                                                               homepage="16"),
                                   group_4=add_contact_form.add_contact_group4(address2="19",
                                                                               phone2="20",
                                                                               notes="21")
                                   )
        wd.find_element_by_link_text("Logout").click()
     #конец теста ###########################################################################################

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
