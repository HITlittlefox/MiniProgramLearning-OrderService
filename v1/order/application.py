# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os


class Application(Flask):
    def __init__(self, import_name, template_folder=None):
        # 父类实现
        super(Application, self).__init__(import_name, template_folder=template_folder, static_folder=None)

        # 切换setting
        self.config.from_pyfile('config/base_setting.py')

        # mac:
        # export ops_config=local
        # win:
        # set ops_config=local
        # set ops_config=base
        # python manager.py runserver
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])

        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd() + "/web/templates")
manager = Manager(app)

'''
函数模板
'''
from common.libs.UrlManager import UrlManager

app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')
