from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def mypage():
    return 'This is my first flask app'

@app.route('/convert_temp')
def convert_temp():
    return render_template('convert.html')

@app.route('/convert_result', methods = ['POST', 'GET'])
def converted():
    if request.method == 'POST':
        value = float(request.form['value_entered'])
        answer = (value * 1.8) + 32
        return render_template('conversion_result.html', value = value, answer = answer)

app.run
