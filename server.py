'''
    File name: server.py
    Author: xdtianyu@gmail.com
    Date created: 2015-01-25 09:56:23
    Date last modified: 2015-01-25 12:52:24
    Python Version: 2.7.3
'''

from flask import Flask
from flask import request

import control
import index

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def root():
    return index.show_index()

@app.route("/control", methods=["GET","POST"])
def show_control():
    if request.method == "POST":
        return control.post(request)
    else:
        return control.show_control()

if __name__ == "__main__":
    app.run(debug=True, host="192.168.4.150", port=5000)
