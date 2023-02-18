# -*- coding: utf-8 -*-
from application import app, db
from flask import Blueprint, g
from common.libs.Helper import ops_render
from common.libs.Helper import getFormatDate
from common.models.stat.StatDailySite import StatDailySite
import datetime

# 蓝图
route_index = Blueprint('index_page', __name__)


# 初始化路由
@route_index.route("/")
def index():
    return ops_render("index/index.html")
