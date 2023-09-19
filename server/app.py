#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:input_string>')
def print_string(input_string):
    # Print the string in the console
    print(input_string)
    # Display the string in the web browser
    return input_string

@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join([str(i) for i in range(num)])  # Use newline characters
    return numbers

@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
