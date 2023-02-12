# -*- coding: utf-8 -*-
from application import app, manager
from flask_script import Server
import www

##web server
# 自定义命令：python manager.py runserver
manager.add_command("runserver",
                    Server(
                        # host='0.0.0.0',
                        port=app.config['SERVER_PORT'],
                        use_debugger=True,
                        use_reloader=True))


def main():
    manager.run()


# 打印所有异常
if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
