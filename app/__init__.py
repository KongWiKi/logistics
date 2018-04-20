'''
@author：KongWeiKun
@file: __init__.py
@time: 18-4-17 下午2:17
@contact: kongwiki@163.com
'''
from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config

mail = Mail()
moment = Moment()
db = SQLAlchemy()
bootstrap=Bootstrap()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = u"请登录！"
login_manager.login_message_category = "info"

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .data import data as data_blueprint
    app.register_blueprint(data_blueprint, url_prefix='/data')

    from .login import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    return app