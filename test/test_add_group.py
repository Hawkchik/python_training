# -*- coding: utf-8 -*-
from python_training.model.group import Group

def test_add_group(app):

    app.group.create(Group(name="1", header="1", footer="1"))


