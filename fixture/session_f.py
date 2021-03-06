# -*- coding: utf-8 -*-
__author__ = 'Maxim.Rumyantsev'


class SessionHelper:

    def __init__(self,app):
        self.app=app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        # login
        self.app.fill_text_field(name="user",send_keys_parameters=username)
        self.app.fill_text_field(name="pass",send_keys_parameters=password)
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def is_logged_in_as(self,username):
        wd = self.app.wd
        #return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"  #1 вариант
        #return wd.find_element_by_xpath("//div/div[1]/form/b").text == "(%s)" % username # можно вот так
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]  # читает текст из окна браузера с круглыми скобочками которые мы отрезаем

    def ensure_login(self,username,password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username,password)

    def logout(self):
        wd = self.app.wd
        # logout
        wd.find_element_by_link_text("Logout").click()

    # если на стринице есть ссылка на логаут, то нажимаем ее
    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0
