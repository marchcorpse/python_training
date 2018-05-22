# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create_contact(Contact(firstname="first", middlename="middle", lastname="last", address="address"))


def test_add_empty_contact(app):
    app.contact.create_contact(Contact(firstname="", middlename="", lastname="", address=""))