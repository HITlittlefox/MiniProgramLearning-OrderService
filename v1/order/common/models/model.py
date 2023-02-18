from peewee import *

database = MySQLDatabase('food_db',
                         **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost',
                            'port': 3306, 'user': 'root', 'password': '123456'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    avatar = CharField(constraints=[SQL("DEFAULT ''")])
    created_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    email = CharField(constraints=[SQL("DEFAULT ''")])
    login_name = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    login_pwd = CharField(constraints=[SQL("DEFAULT ''")])
    login_salt = CharField(constraints=[SQL("DEFAULT ''")])
    mobile = CharField(constraints=[SQL("DEFAULT ''")])
    nickname = CharField(constraints=[SQL("DEFAULT ''")])
    sex = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    uid = BigAutoField()
    updated_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'user'
