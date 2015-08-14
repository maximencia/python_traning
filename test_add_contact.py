# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import datetime, unittest
from group import contact_SECONDARY_info,create_contact_info2_telephone_and_email

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
    
    def test_(self):
        success = True

    #начало теста ###########################################################################################
        wd = self.wd
        self.go_to_homepage(wd)
        self.login(wd, "admin", "secret")
        self.open_new_contact_form(wd)

    # fill new contact form
        self.create_contact_info1(wd)
        self.create_contact_info2_telephone_and_email(wd,home="8",mobile="8",work="8",fax="8",email2="8",email3="8",homepage="8")
        #даты
        self.create_contact_date_info(wd)
        self.create_contact_SECONDARY_info(wd, contact_SECONDARY_info(address2="17",phone2="19",notes="18"))

        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)
     #конец теста ###########################################################################################



    def create_contact_SECONDARY_info(self, wd, contact_SECONDARY_info):
        # SECONDARY
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact_SECONDARY_info.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact_SECONDARY_info.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact_SECONDARY_info.notes)

    # from selenium.webdriver.support.ui import Select
    # select = Select(b.find_element_by_xpath("//div[@id='content']/form/select[3]"))
    # select.select_by_visible_text(....)
    def create_contact_date_info(self, wd):
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2015")

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[18]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[18]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2016")

    def create_contact_info2_telephone_and_email(self, wd, home, mobile, work, fax, email2, email3, homepage):
        # telephon & emails
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax)
        # email # 1 заполняется автоматически
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)

    def create_contact_info1(self, wd):
        # CONTACT_INFO
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("100")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("200")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("lastname_"+str(now_time))
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("4")
        # пропущено добавление фото
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("5")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("6")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("7")

    def open_new_contact_form(self, wd):
        # add_new_contact_form
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, login, password):
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

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
