# -*- coding: utf-8 -*-
import pytest
from python_training.group import Group
from python_training.application import Application




@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_test_add_group(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.open_group_page()
        app.create_group( Group(name="1", header="1",footer= "1"))
        app.return_group_page()
        app.logout()

