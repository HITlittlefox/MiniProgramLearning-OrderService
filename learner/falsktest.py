# http://127.0.0.1:5000/
from flask import Flask, url_for, render_template
from imooc import route_imooc
from common.libs.UrlManager import UrlManager
import pandas

app = Flask(__name__)

app.register_blueprint(route_imooc, url_prefix="/imooc")

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/food_db"
# initialize the app with the extension
db = SQLAlchemy(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


@app.route('/api/hello')
def hello():
    from sqlalchemy import text
    # sql = text("SELECT * FROM user")
    sql = text("SHOW FULL TABLES FROM `Engine(mysql+cymysql://root:***@localhost:3306/food_db)`")
    result = db.engine.connect().execute(sql)
    for row in result:
        app.logger.info(row)
    return 'Hello, World'


@app.route('/')
def hello_world():
    url = url_for("index")
    url_1 = UrlManager.buildUrl("/api")
    url_2 = UrlManager.buildStaticUrl("/css/bootstrap.css")

    msg = "i'm a bug"
    app.logger.error(msg)
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')

    return msg


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return 'This page does not exist', 404


@app.route('/api')
def index():
    return 'Index Page'


if __name__ == '__main__':
    app.run(debug=True)
