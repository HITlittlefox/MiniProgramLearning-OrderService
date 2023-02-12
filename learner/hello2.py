from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/mysql"
# initialize the app with the extension
db = SQLAlchemy(app)


@app.route('/api/hello')
def hello():
    from sqlalchemy import text
    sql = text("SELECT * FROM user")
    result = db.engine.connect().execute(sql)
    for row in result:
        app.logger.info(row)
    return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True)
