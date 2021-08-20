from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Dojo'


@app.route('/say/<name>') 
def say(name):
    print(name)
    return f"Hi {name}!"

@app.route('/repeat/<num>/<name>')
def  repeat(num,name):
    return f"{name} " * int(num)


if __name__ =='__main__':
    app.run(debug=True)