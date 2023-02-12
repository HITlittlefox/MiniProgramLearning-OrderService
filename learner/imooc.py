from flask import Blueprint
route_imooc = Blueprint("imooc page", __name__)


@route_imooc.route("/")
def index():
    return "imooc index page"


@route_imooc.route("/hello")
def hello():
    return "imooc hello world"
