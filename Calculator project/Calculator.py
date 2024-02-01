from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        op = request.form['operator']
        num2 = float(request.form['num2'])

        result = None

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "/":
            result = num1 / num2
        elif op == "*":
            result = num1 * num2
        else:
            return render_template('index.html', error="Invalid operator")

        return render_template('index.html', result=result)

    except ValueError:
        return render_template('index.html', error="Invalid input")

if __name__ == '__main__':
    app.run(debug=True)
