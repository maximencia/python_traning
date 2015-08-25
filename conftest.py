# -*- coding: utf-8 -*-
import pytest,datetime
from fixture.application import Application

now_time = datetime.datetime.now()

@pytest.fixture
def app(request):
    fixture = Application()
    fixture.session.login(username="admin",password="secret")
    def final():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(final)
    return fixture