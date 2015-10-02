# -*- coding: utf-8 -*-
__author__ = 'Maxim.Rumyantsev'
import re
from random import randrange
from model.contact import Contact

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

# прямая проверка - это когда мы режем
# обратная проверка - когда мы склеиваем и проверяем
# map - возможность применить какую то функцию, ко всем элементам списка
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="", # отфильтровываем пустые строки
                            (map(lambda x: clear(x), # применяем функцйию удаления () и -
                                 filter(lambda x: x is not None, # убираем все None
                                        [contact.home,contact.mobile,contact.work,contact.fax])))))

#Задание №14: Реализовать проверки для всех полей контакта на главной странице
#Реализовать тест, который проверяет, что для некоторого одного случайно выбранного контакта информация на главной странице
# (в таблице) соответствует информации, представленной в форме редактирования контакта (где задаются все его свойства),
# при этом проверяться должны все представленные свойства -- имя, фамилия, адрес, телефоны, адреса электронной почты.
#Для телефонов и адресов электронной почты используйте технику обратных проверок.
def test_assert_contact_info_home_and_edit_page(app):
    old_contacts =  app.contact.get_contacts_list()
    index=randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contacts_list()[index] # берем первый из загруженных контактов
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",#удаляем пустые строки
                            filter(lambda x: x is not None,# удаляем все None
                                   [contact.email1, contact.email2, contact.email3])))


#Задание №21: Переделать тесты для проверки информации о контактах на главной странице

#Переделать тесты для проверки информации о контактах на главной странице -- на этот раз нужно реализовать сравнение
# для всех записей, а не для одной случайно выбранной. А сравнивать -- с информацией, загруженной из базы данных.
def test_assert_contact_info_home_and_db_for_all_contact(app,db):
    contact_from_home_page= app.contact.get_contacts_list()
    contact_from_db = db.get_contacts_list()
    web=sorted(contact_from_home_page, key=Contact.id_or_max)
    db= sorted(contact_from_db,        key=Contact.id_or_max)
    assert web == db






