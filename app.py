from flask import Flask, render_template, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getTempLog')
def getTempLog():
    return ["0", "1", "2"]


@app.route('/getTemp')
def getTemp():
    return "0"


@app.route('/getFeedLog')
def getFeedLog():
    return ["9", "8", "7"]


@app.route('/feed')
def feed():
    return "done"


if __name__ == '__main__':
    app.run(DEBUG=True)
