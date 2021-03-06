

#通用配置
class Config(object):

    #bootstrap使用本地的静态文件
    BOOTSTRAP_SERVE_LOCAL = True


#开发环境
class DevelopmentConfig(Config):
    pass

#测试环境
class TestingConfig(Config):
    pass

#生产环境
class ProductionConfig(Config):
    pass

config = {
    'test':TestingConfig,
    'product':ProductionConfig,
    'default':DevelopmentConfig,
}
