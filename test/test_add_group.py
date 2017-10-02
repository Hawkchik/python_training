# -*- coding: utf-8 -*-
import pytest

from python_training.fixture.application import Application
from python_training.model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.group.open_group_page()
        app.group.create(Group(name="1", header="1", footer="1"))
        app.group.return_group_page()
        app.session.logout()

