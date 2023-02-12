# -*- coding: utf-8 -*-
from application import app
from web.controllers.index import route_index

# 路由注入
app.register_blueprint(route_index, url_prefix="/")