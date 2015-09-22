# -*- coding: utf-8 -*-
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class ORMFixture:

    db=Database()

    class ORMGroup(db.Entity):
        _table_  = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        #добавляем связь
        contacts= Set(lambda: ORMFixture.ORMContact, table="address_in_groups" , column="id", reverse="groups", lazy=True)


    class ORMContact(db.Entity):
        _table_  = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")
        #добавляем связь
        groups= Set(lambda: ORMFixture.ORMGroup, table="address_in_groups" , column="group_id", reverse="contacts", lazy=True)


    # из за ошибки ниже pymysql может преобразовывать невалидные даты но PONY принудительно ей запрещает , а мы разрешим  conv=decoders)
    #File "C:\python_traning\python_traning\env\lib\site-packages\pony\orm\dbapiprovider.py", line 53, in wrap_dbapi_exceptions
    #except dbapi_module.OperationalError as e: raise OperationalError(e)
    def __init__(self, host, name, user, password):
        self.db.bind("mysql", host=host, database=name, user=user, password=password,conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)


    def convert_group_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    #@db_session
    def get_group_list(self):
        with db_session:
            return self.convert_group_to_model(select(g for g in ORMFixture.ORMGroup)) #SELECT `g`.`group_id`, `g`.`group_name`, `g`.`group_header`, `g`.`group_footer` FROM `group_list` `g`

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    def get_contact_list(self):
        with db_session:
            return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None)) # SELECT * FROM `addressbook` `c` WHERE `c`.`deprecated` IS NULL

    @db_session
    def get_contacts_in_group(self,group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)


    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))









# c:\python_traning\python_traning\env>Scripts\activate
# (env) c:\python_traning\python_traning\env>pip install pony
# Collecting pony
# c:\python_traning\python_traning\env\lib\site-packages\pip\_vendor\requests\packages\urllib3\util\ssl_.py:90: InsecurePlatformWarning: A true SSLConte
# xt object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more informati
# on, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
#   InsecurePlatformWarning
#   Downloading pony-0.6.1.tar.gz (287kB)
#     100% |################################| 290kB 682kB/s
# Building wheels for collected packages: pony
#   Running setup.py bdist_wheel for pony
#   Stored in directory: C:\Users\Maxim.Rumyantsev\AppData\Local\pip\Cache\wheels\69\5f\36\f5932bace1fbc845d198fe12103df8a832133f326f0834788e
# Successfully built pony
# Installing collected packages: pony
# Successfully installed pony-0.6.1
#
# (env) c:\python_traning\python_traning\env>pip install pymysql
# Collecting pymysql
# c:\python_traning\python_traning\env\lib\site-packages\pip\_vendor\requests\packages\urllib3\util\ssl_.py:90: InsecurePlatformWarning: A true SSLConte
# xt object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more informati
# on, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
#   InsecurePlatformWarning
#   Downloading PyMySQL-0.6.6-py2.py3-none-any.whl (66kB)
#     100% |################################| 69kB 803kB/s
# Installing collected packages: pymysql
# Successfully installed pymysql-0.6.6