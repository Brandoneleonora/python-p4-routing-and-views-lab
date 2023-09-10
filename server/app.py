#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:word>')
def print_string(word):
    print(f'{word}')
    return f'{word}'
    
@app.route('/count/<int:number>')
def cnt(number):
    return f'{number-10}\n{number-9}\n{number-8}\n{number-7}\n{number-6}\n{number-5}\n{number-4}\n{number-3}\n{number-2}\n{number-1}\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):
    print(num1 + num2)
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '%':
        return f'{num1 % num2}'
    elif operation == 'div':
        return f'{num1 / num2}'
    elif operation == '*':
        return f'{num1 * num2}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
