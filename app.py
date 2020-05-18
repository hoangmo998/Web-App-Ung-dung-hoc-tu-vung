from flask import *
import bcrypt
from models.user import User
import mlab

app = Flask(_name_)
app.secret_key = 'mysecret'
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/navigation')
def navigation():
    user = session.get('username')
    return render_template("navigation.html",
                            user=user,
                          )

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
       return render_template("login.html")
    elif request.method == "POST":
        form = request.form 
        username = form["username"]
        password = form["pass"]
    login_user = User.objects(username=username).first() 
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            session['password'] = request.form['pass']
            if session['username'] == "admin" and session['password'] == "admin":
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('#'))
    flash('Username or password wrong! Please try again!')
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
         return render_template('register.html')
       
    if request.method == 'POST':
        existing_user = User.objects(username = request.form["username"]).first()

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users = User(
                username = request.form['username'], 
                password = hashpass
                )
            users.save()
            session['username'] = request.form['username']
            return redirect(url_for('login'))
        if existing_user:
            flash('Username address already exists')
            return redirect(url_for('register'))

@app.route('/logout')
def logout():
    del session["username"]
    return redirect("/login")