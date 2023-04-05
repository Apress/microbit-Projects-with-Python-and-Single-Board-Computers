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
        calculation = request.form['conversion']
        value = float(request.form['value_entered'])
        if calculation == 'c2f':
            answer = (value * 1.8) + 32
            units = 'farenheit'
        elif calculation == 'f2c':
            answer = (value - 32)/1.8
            units = 'celcius'
        return render_template('conversion_result.html', answer = answer, units = units)
    else:
        return render_template('error.html')
app.debug = True
app.run('0.0.0.0')
