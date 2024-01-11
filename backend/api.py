
from flask import Flask,request,jsonify
import subprocess
import os
#import threading



app = Flask(__name__)
process = None


@app.route("/", methods=['GET'])
def home():
    global process
    if process is None or process.poll() is not None:
        process = subprocess.Popen(['python', 'alexa.py'])
        return 'Model started.'
    else:
        return 'Model already running.'

@app.route('/stop', methods=['POST'])
def stop():
    global process
    if process is not None and process.poll() is None:
        process.terminate()
        process.wait()
        process = None
        return 'Model stopped.'
    else:
        return 'Model not running.'

if __name__ == "__main__":
    app.run()