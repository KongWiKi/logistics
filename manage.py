'''
@author：KongWeiKun
@file: manage.py
@time: 18-4-17 下午2:27
@contact: kongwiki@163.com
'''
from app import create_app, db
from flask_script import Manager,Shell,Server
from flask_migrate import Migrate, MigrateCommand

from app.models import  User
app = create_app('default')
manager = Manager(app)
migtate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,
                db=db,
                User=User,
                Server=Server)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)

@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run(debug=True,port=4000)
    # manager.run()