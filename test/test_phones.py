# -*- coding: utf-8 -*-
__author__ = 'Maxim.Rumyantsev'
import re

def test_phone_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0] # берем первый из загруженных контактов
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0) # а тут берем по индексу
    assert contact_from_home_page.home == clear(contact_from_edit_page.home)
    assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_home_page.work == clear(contact_from_edit_page.work)
    assert contact_from_home_page.fax == clear(contact_from_edit_page.fax)

def clear(s):
    return re.sub("[() -]", "", s)
