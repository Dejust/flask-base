from flask_migrate import MigrateCommand
from flask_script import Manager

from app.container import APP

manager = Manager(APP)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
