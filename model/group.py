__author__ = 'Maxim.Rumyantsev'

class Group:

    def __init__(self,name,header,footer):
        self.name=name
        self.header=header
        self.footer=footer


class Contact:

    def __init__(self,firstname, middlename, lastname, nickname, title, company, address,home,mobile,work,fax,email2,email3,homepage,address2,phone2,notes):
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



