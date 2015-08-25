# -*- coding: utf-8 -*-
import pytest,datetime
from fixture.application import Application

now_time = datetime.datetime.now()

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.fixture_is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin",password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def final():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(final)
    return fixture
