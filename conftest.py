# -*- coding: utf-8 -*-
import pytest,datetime,json,os.path
from fixture.application import Application
import importlib,jsonpickle
from fixture.db import DbFixture

now_time = datetime.datetime.now()

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    #читаем из файла конфигурации все что касается web
    web_config = load_config(request.config.getoption("--target"))['web']
    # если фикстура не создана или невалидна то создаем ее
    if fixture is None or not fixture.fixture_is_valid():
        fixture = Application(browser=browser,base_url=web_config['base_url'])
    fixture.session.ensure_login(username=web_config['username'],password=web_config['password'])
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
    parser.addoption("--target", action="store", default="target.json") # имя файла с опциями по умолчанию
    parser.addoption("--check_ui", action="store_true")

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            p=fixture[5:]
            # загружаем данные из модуля например из C:\python_traning\python_traning\data\groups.py
            testdata = load_from_module(fixture[5:]) # отрежем первые 5 символов
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        if fixture.startswith("json_"):
            p=fixture[5:]
            # загружаем данные из файла
            testdata = load_from_json(fixture[5:]) # отрежем первые 5 символов
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

@pytest.fixture(scope="session")
def db(request):
    #читаем из файла конфигурации все что касается db
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture=DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password']) # сделан класс DbFixture
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


# функция загрузки из файла
def load_config(from_file):
    global target
    if target is None:
        path_to_config = os.path.join(os.path.dirname(os.path.abspath(__file__)),from_file)
        with open(path_to_config) as config_file:
            target=json.load(config_file)
    return target


