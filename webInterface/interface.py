from threading import Thread
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from webInterface.transmitter import sendCmd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('moveHand') == 'moveHand':
            sendCmd("moveLeftHand")
    return render_template('index.html')

#app.run(debug=False)

flaskThread = Thread(target=app.run)