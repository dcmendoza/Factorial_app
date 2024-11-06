from flask import Flask, render_template, request

app = Flask(__name__)

def factorial(n):
    """Calcula el factorial de un número."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/factorial_result', methods=['POST'])
def factorial_result():
    num = int(request.form['number'])
    result = factorial(num)
    return render_template('result.html', number=num, result=result)

if __name__ == '__main__':
    app.run(debug=True)
