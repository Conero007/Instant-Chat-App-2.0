from flask import Flask
from .database import get_user
from flask_socketio import SocketIO
from flask_login import LoginManager

ROOMS = ['global', 'help']


def create_app():
    global socketio, app

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "thisisademoversion"

    socketio = SocketIO(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(email):
        return get_user(email)

    return socketio, app
