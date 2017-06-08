from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submitName():
    name = request.form['name']
    print 'I know your name is ' + name
    return redirect('/')

app.run(debug=True)
# Nothing after the debug line will be read.
