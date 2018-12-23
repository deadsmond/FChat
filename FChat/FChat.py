# https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

from flask import Flask, render_template, json, request, redirect
from sys import executable, argv
from subprocess import Popen, CREATE_NEW_CONSOLE

_port = sys.argv[1]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def signUp():
    # read the posted values from the UI
    _name = request.form['inputName']
    _room = request.form['inputRoom']
 
    # validate the received values
    if _name and _room:
        # create room
        Popen([executable, 'session/session.py ' + _room + " " + _port],
              creationflags=CREATE_NEW_CONSOLE)
        # forward to the room
        return redirect("0.0.0.0:" + _port + "/" + _room, code=302)
    else:
        return json.dumps({'html':'<span>bad</span>'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=_port)
