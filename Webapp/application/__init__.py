from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

app.secret_key = 'your_secret_key'


from application import routes
