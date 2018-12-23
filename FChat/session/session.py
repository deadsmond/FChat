from flask import Flask, render_template
from flask_socketio import SocketIO

import sys
_room = sys.argv[1]
_port = sys.argv[2]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/' + _room)
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print(*list(json.values()))
    # with open('logs/' + _room + '.txt', 'a') as file:
    #    file.write(' '.join(list(json.values())) + "\n")
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True, port = _port)
