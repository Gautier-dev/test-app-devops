from flask import Flask
import os

app = Flask(__name__)
message = "Hello World" if os.environ.get('message') == None else os.environ.get("message") 


@app.route("/")
def hello_world():
    return "<p>{}</p>".format(message)

