from flask_script import Manager
from apps import create_app

app = create_app('product')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()