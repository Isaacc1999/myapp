# Flask app for Azure devops exercise
# Syntactical errors have been included
from flask import Flask, request
import socket
import os
def square(n):
    number = float(n)
    return 'Square of {} is {}'.format(number, number*number)
app = Flask(__name__)
# Use the following url to get the result reaplicing <IP> with the external IP http://<IP>:5000/
@app.route('/')
def hello_world():
    # to get the hostname
    host = socket.gethostname()
    # to get the host ip
    ip = socket.gethostbyname(host)
    message = os.getenv('MESSAGE', 'Flask Demo')
    return '{} on host {} ({})'.format(message, host, ip)
# Use the following url to get the result reaplicing <IP> with the external IP http://<IP>:5000/square_number?number=2
@app.route('/square_number')
def square_number():
    return square(request.args.get('number'))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
