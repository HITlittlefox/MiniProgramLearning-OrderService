# -*- coding: utf-8 -*-
from flask import Blueprint

# 蓝图
route_index = Blueprint('index_page', __name__)


# 初始化路由
@route_index.route("/")
def index():
    return "Hello World"
