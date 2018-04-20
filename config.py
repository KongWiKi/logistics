'''
@author：KongWeiKun
@file: config.py
@time: 18-4-17 下午2:27
@contact: kongwiki@163.com
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY='42ehhfsfdsqry298f29tygh3qt'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com',
    MAIL_PROT = 465,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'kongwiki@163.com',
    MAIL_PASSWORD = '....',
    MAIL_DEBUG = True
    SQLALCHEMY_DATABASE_URI =  \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

# # class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
#         'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
#
#
# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
#         'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development' : DevelopmentConfig,
    # 'testing': TestingConfig,
    # 'production': ProductionConfig,
    'default': DevelopmentConfig
}