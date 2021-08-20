from flask import Flask , redirect, render_template, session
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')          
def counter():
    if  'counter'not  in session:
        session['counter']= 0
    else:
        session['counter'] += 1
    counter = session["counter"]
    return render_template('counter.html', counter = counter)
    
    

@app.route('/show') 
def reset():
    session.clear()
    return redirect('/')

@app.route('/view' ) 
def add2():
    session['counter'] += 1
    return redirect('/')
    

if __name__=="__main__":       
    app.run(debug=True)    
