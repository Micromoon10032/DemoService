import servicehub
import flask
import gevent.pywsgi

app = flask.Flask(__name__)

ctx = servicehub.Context("172.16.8.1:6619")
ctx.register("hydrocloud_demo_service", "http://172.16.9.6", True)

@app.route("/")
def on_root():
    return "Hello world"

server = gevent.pywsgi.WSGIServer(("127.0.0.1", 9127), app)
server.serve_forever()
