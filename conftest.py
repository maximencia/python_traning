# -*- coding: utf-8 -*-
import pytest,datetime
from fixture.application import Application

now_time = datetime.datetime.now()

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture