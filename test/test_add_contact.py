# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import add_contact_form


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
      # # fill new contact form
    #     form_add_contact_
    #                      _group1  (main info)
    #                             firstname
    #                             middlename
    #                             lastname
    #                             nickname
    #                             # пропущено добавление фото
    #                             title
    #                             company
    #                             address

    #                      _group2  (telephon & emails)
    #                             home
    #                             mobile
    #                             work
    #                             fax
    #                             # email # 1 заполняется автоматически
    #                             email2
    #                             email3
    #                             homepage

    #                      _group3  (date & group)
    #                             birthday
    #                             anniversary
    #                             # должна выбираться группа group
    #                      _group4  (secondary )
    #                             address2
    #                             phone2
    #                             notes
def test_add_contact(app):
    app.session.login(username="admin",password="secret")

    app.fill_add_contact_form( group_1=add_contact_form.add_contact_group1(firstname="1",
                                                                          middlename="2",
                                                                          lastname=("lastname_" + str(app.time_now)),
                                                                          nickname="4",
                                                                          title="6",
                                                                          company="7",
                                                                          address="8"),
                                group_2=add_contact_form.add_contact_group2(home="9",
                                                                             mobile="10",
                                                                            work="11",
                                                                            fax="12",
                                                                            email2="14",
                                                                            email3="15",
                                                                            homepage="16"),
                                group_4=add_contact_form.add_contact_group4(address2="19",
                                                                            phone2="20",
                                                                            notes="21")
                       )
    app.session.logout()
