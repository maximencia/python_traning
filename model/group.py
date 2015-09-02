__author__ = 'Maxim.Rumyantsev'
# -*- coding: utf-8 -*-

from sys import maxsize

class Group:

    def __init__(self,
                 name=None,
                 header=None,
                 footer=None,
                 id=None):
        self.name=name
        self.header=header
        self.footer=footer
        self.id=id

    def __repr__(self):
        return "%s%s" % (self.id,self.name)

    # сравнение по смыслу а не по физическому расположению объектов
    def __eq__(self, other):
        # в случае если идендификатор не определен он не учитывался при сравнении
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    # вычисляем по группе ключ используемый для сравнения
    # если у группы есть id то а если его нет то возвращается большое число maxsize (максимальное целое число)
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize






class Contact:

    def __init__(self,firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 home=None,mobile=None,work=None,fax=None,email2=None,email3=None,homepage=None,address2=None,phone2=None,notes=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address

        self.home=home
        self.mobile=mobile
        self.work=work
        self.fax=fax
        #self.email1=email1
        self.email2=email2
        self.email3=email3
        self.homepage=homepage

        self.address2=address2
        self.phone2=phone2
        self.notes=notes




