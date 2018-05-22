# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create_group(Group(name="sdsd", header="sds", footer="sdsda"))


def test_add_empty_group(app):
    app.group.create_group(Group(name="", header="", footer=""))
