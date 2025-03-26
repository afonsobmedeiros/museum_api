from bottle import Bottle
from jwt_bottle.JWTPlugin import JWTPlugin
from domain.models.Auth import Auth


def install(app: Bottle):
    config = {'model': Auth, 'endpoint': '/auth', 'auth_name': "auth", 'refresh_name': 'refresh'}
    jwt = JWTPlugin("a-string-secret-at-least-256-bits-long", config=config, payload=['id', 'email', 'name'])
    app.install(jwt)