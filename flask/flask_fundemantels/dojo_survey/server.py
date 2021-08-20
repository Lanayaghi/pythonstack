from ast import copy_location
from flask import Flask, render_template,request
app = Flask(__name__)



@app.route('/')
def index():
    return render_template("survey.html")



@app.route('/result', methods = ['post'])
def create_user():
    print('Got Post INfo')
    print(request.form)
    return render_template("new.html", name=request.form['name'], location=request.form['location'], fave=request.form['fave'], comment = request.form['comment'])

    


if __name__ == "__main__":
    app.run(debug=True)
