from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
from wsgiref import simple_server
import os

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
    
    return "Just attempting to connect"

port = int(os.getenv("PORT", 5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on http://127.0.0.1:5000/")
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()


    # app.run(debug=True)