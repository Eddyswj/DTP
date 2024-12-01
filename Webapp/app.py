from application import app, socketio  

if __name__ == '__main__':
    socketio.run(application, host='0.0.0.0', port=8000)