# -*- coding: utf-8 -*-

from python_training.model.group import Group




def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.group.open_groups_page()
        app.group.create(Group(name="1", header="1", footer="1"))
        app.session.logout()

