# -*- coding: utf-8 -*-
import pytest,datetime,json,os.path
from fixture.application import Application
import importlib

now_time = datetime.datetime.now()

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")

    if target is None:
        path_to_config = os.path.join(os.path.dirname(os.path.abspath(__file__)),request.config.getoption("--target"))
        with open(path_to_config) as config_file:
            target=json.load(config_file)
    # если фикстура не создана или невалидна то создаем ее
    if fixture is None or not fixture.fixture_is_valid():
        fixture = Application(browser=browser,base_url=target['base_url'])
    fixture.session.ensure_login(username=target['username'],password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def final():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(final)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

# def pytest_generate_tests(metafunc):
#     for fixture in metafunc.fixturenames:
#         if fixture.startswith("data_"):
#             testdata= load_form_module(fixture[5:])  # отрежем первые 5 символов
#             metafunc.parametrize(fixture,testdata,ids=[str(x) for x in testdata])

# def load_form_module(module):
#     p=importlib.import_module("data.%s" % module).testdata
#     return importlib.import_module("data.%s" % module).testdata
def load_form_module(module):
    return importlib.import_module("data.%s" % module).testdata

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            p=fixture[5:]
            testdata = load_form_module(fixture[5:]) # отрежем первые 5 символов
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
