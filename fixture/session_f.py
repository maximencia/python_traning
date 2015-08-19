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
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.wd
        # logout
        wd.find_element_by_link_text("Logout").click()
