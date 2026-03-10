from flask import Flask, render_template
from flask_sock import Sock
app = Flask(__name__)
sock = Sock(app)
clients = []
@app.route('/')
def index():
    return render_template('index.html')
@sock.route('/ws')
def websocket(ws):
    clients.append(ws)
    try:
        while True:
            message = ws.receive()
            if message:
                # Broadcast to all connected clients
                for client in clients:
                    client.send(message)
    except:
        clients.remove(ws)
if __name__ == '__main__':
    app.run(debug=True)