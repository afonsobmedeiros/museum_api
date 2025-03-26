from bottle import Bottle

from .extensions import install_jwt_extension


def create_app():
    app = Bottle()
    
    install_jwt_extension.install(app)
    
    return app