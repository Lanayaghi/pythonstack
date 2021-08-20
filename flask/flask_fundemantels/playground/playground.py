from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def hello_world():
    return render_template("index.html", num=3, color="lightblue")

@app.route("/play/<num>")
def square(num):
    return render_template("index.html", num=int(num))

@app.route("/play/<num>/<color>")
def color(num,color):
    return render_template("index.html", num=int(num), color=color)

if __name__ =="__main__":
    app.run(debug=True)
