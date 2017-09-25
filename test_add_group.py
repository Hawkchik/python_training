# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from python_training.group import Group
from python_training.Application import Application
import pytest

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
        app.app.open_home_page()
        app.app.login(username="admin", password="secret")
        app.app.open_group_page()
        app.app.create_group( Group(name="1", header="1",footer= "1"))
        app.app.return_group_page()
        app.app.logout()




