from flask import Flask
app = Flask(__name__)

#import sensor
from sensor import get_cpu_temperature

@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/cpu_temp')
def cpu_temp():
    temp = format(get_cpu_temperature(), '.2f')
    return 'CPU Temperature: {}°C'.format(temp)