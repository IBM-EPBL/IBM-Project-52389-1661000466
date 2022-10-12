from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session, render_template_string
from markupsafe import escape
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/singin')
def signin():
  return render_template('singin.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/logout')
def logout():
  return render_template('logout.html')

@app.route('/aboutus')
def aboutus():
  return render_template('about us.html')

def get_db():
    conn = sql.connect('studentss.db')
    conn.row_factory = sql.Row
    return conn

@app.route('/signup',methods = ['POST', 'GET'])
def signup_page():
  if request.method == 'POST':
    try:
        email = request.form['email']
        password = request.form['password']
        repeatPassword = request.form['repeatPassword']
        with sql.connect("studentss.db") as con:
         cur = con.cursor()
         cur.execute("INSERT INTO customers (email,password,repeatPassword) VALUES (?,?,?)",(email,password,repeatPassword) )
         con.commit()
         msg = "Record successfully added!"
    except:
      con.rollback()
      msg = "error in insert operation"

    finally:
      return render_template("home.html",msg = "created")
      con.close()

@app.route('/singin', methods=('GET', 'POST'))
def signin_page():
    error = None
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        db = get_db()
        user = db.execute(
            'SELECT password FROM customers WHERE email = ?', (username, )
        ).fetchone()
        
        if user is None:
            error = 'Incorrect Username/Password.'
        elif password != user['password']:
            print(user)
            error = 'Incorrect Password.'

        if error is None:
            return render_template("logout.html")
        db.close()

    return render_template('singin.html', title='Sign In', error=error)

@app.route('/logout', methods=('GET', 'POST'))
def logout_page(nme, adrss):
    error = None
    if request.method == 'POST':
        username = request.form['email']
        return render_template('logout.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)