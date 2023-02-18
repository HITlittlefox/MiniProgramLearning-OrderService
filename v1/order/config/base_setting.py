# -*- coding: utf-8 -*-
DEBUG = False
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SERVER_PORT = 8999
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/food_db'
AUTH_COOKIE_NAME = "mooc_food"

# SEO_TITLE = "Python Flask构建微信小程序订餐系统"
# 过滤url
# 非/user/login 全部过滤
IGNORE_URLS = [
    "^/user/login"
]
# "^/api"
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

# 分页情况
PAGE_SIZE = 50
PAGE_DISPLAY = 10

# 会员情况
STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除"
}
# 小程序
MINA_APP = {
    'appid': 'wxd47addbb7d257b3c',
    'appkey': 'c4fbacc50efa192eb805faaea43ddc2b',
    # 'paykey': 'xxxxxxxxxxxxxx换自己的',
    # 'mch_id': 'xxxxxxxxxxxx换自己的',
    'callback_url': '/api/order/callback'
}

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    # 'prefix_path': '\\web\\static\\upload\\',
    # 'prefix_url': '\\static\\upload\\'
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}

APP = {
    'domain': 'http://127.0.0.1:8999'
}

#
PAY_STATUS_MAPPING = {
    "1": "已支付",
    "-8": "待支付",
    "0": "已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0": "订单关闭",
    "1": "支付成功",
    "-8": "待支付",
    "-7": "待发货",
    "-6": "待确认",
    "-5": "待评价"
}
