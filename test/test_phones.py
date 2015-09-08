# -*- coding: utf-8 -*-
__author__ = 'Maxim.Rumyantsev'
import re

# проверям что информация о телефоназ на главной странице совпадает с информацие телефонов на форме редактирования
def test_phone_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0] # берем первый из загруженных контактов
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0) # а тут берем по индексу
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


# проверям что информация о телефоназ на странице с детальной информацией совпадает с информацие телефонов на форме редактирования
def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.fax == contact_from_edit_page.fax


def clear(s):
    return re.sub("[() -]", "", s)

# map - возможность применить какую то функцию, ко всем элементам списка
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="", # отфильтровываем пустые строки
                            (map(lambda x: clear(x), # применяем функцйию удаления () и -
                                 filter(lambda x: x is not None, # убираем все None
                                        [contact.home,contact.mobile,contact.work,contact.fax])))))