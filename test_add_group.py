# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from python_training.group import Group
from python_training.application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app=Application()
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_test_add_group(self):
        wd = self.wd
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.open_group_page()
        self.app.create_group( Group(name="1", header="1",footer= "1"))
        self.app.return_group_page()
        self.app.logout()



    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
