from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)
coffee_pot = 29

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        GPIO.output(coffee_pot, GPIO.HIGH)
        return 'Brewing coffee...'
    return render_template('index.html')

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(coffee_pot, GPIO.OUT)
    GPIO.output(coffee_pot, GPIO.LOW)
    app.run(host='0.0.0.0')
