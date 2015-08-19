__author__ = 'Maxim.Rumyantsev'

class Group:

    def __init__(self,name,header,footer):
        self.name=name
        self.header=header
        self.footer=footer


class add_contact_form:
    def __init__(self,add_contact_group1,add_contact_group2,add_contact_group4):
         self.add_contact_group1=add_contact_group1
         self.add_contact_group2=add_contact_group2
         self.add_contact_group4=add_contact_group4

    class add_contact_group1:
        def __init__(self,firstname, middlename, lastname, nickname, title, company, address):
            self.firstname=firstname
            self.middlename=middlename
            self.lastname=lastname
            self.nickname=nickname
            self.title=title
            self.company=company
            self.address=address

    class add_contact_group2:
        def __init__(self,home,mobile,work,fax,email2,email3,homepage):
            self.home=home
            self.mobile=mobile
            self.work=work
            self.fax=fax
            #self.email1=email1
            self.email2=email2
            self.email3=email3
            self.homepage=homepage

    class add_contact_group4:
        def __init__(self,address2,phone2,notes):
            self.address2=address2
            self.phone2=phone2
            self.notes=notes




