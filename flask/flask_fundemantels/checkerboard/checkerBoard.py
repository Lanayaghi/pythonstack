from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',checker=int(8),ghazal=int(8))

@app.route('/<num>')
def index2(num):
    return render_template('index.html',checker=int(8),ghazal=int(num))

@app.route('/<num1>/<num2>')
def index3(num1,num2):
    return render_template('index.html',checker=int(num1),ghazal=int(num2))


if __name__=="__main__":
    app.run(debug=True)