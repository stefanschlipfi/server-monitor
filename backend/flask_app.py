from flask import Flask,render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'J$eEV§0uzGzjRxTC$DM2LKy!'

#websocket
from flask_socketio import SocketIO, emit
socketio = SocketIO(app,cors_allowed_origins='*',async_mode="threading")

#import logger
from utils import *
logger_name = 'flask_views'
init_logger(loglevel='DEBUG',filename='flask_views.log',logger_name=logger_name)
import logging
logger = logging.getLogger(logger_name)

#import CPU Thread from thread.py
from thread import TempThread

#Websocket Way
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/ws_cpu_temp')
def test_connect():
    logger.debug("Connected with socket.io")
    thread = TempThread(socketio=socketio,namespace='/ws_cpu_temp')
    thread.start()

@socketio.on('disconnect', namespace='/ws_cpu_temp')
def test_disconnect():
    logger.debug("Client disconnected")


@app.route('/chat')
def chat():
    return render_template('chat.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    logger.debug("Connected with socket.io")
    emit('my reponse', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    logger.debug("Client disconnected")

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message_broadcast(message):
    emit('my response', {'data': message['data']}, broadcast=True)

if __name__ == "__main__":
   
    import eventlet
    eventlet.monkey_patch()

    socketio.run(app)

    