from flask import *
import bcrypt
from models.user import User
from models.vegetablesFruits import Vegetablesfruits
import mlab

app = Flask(__name__)
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
                return redirect(url_for('learn'))
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

@app.route('/learn')
def learn():
    user = session.get('username')
    return render_template("learn.html",
                            user = user,
                           )

@app.route('/vegetablesAndFruits')
def vegetablesAndFruits():
    user = session.get('username')
    list_audio = []
    list_word  = []
    list_image = []
    list_pronunciation = []
    list_id = []
     # get all document from dabase
    total_vegetablesAndFruits = Vegetablesfruits.objects()
    for i in total_vegetablesAndFruits:
        audio = i.audio_link
        word  = i.word
        image = i.image
        pronunciation = i.pronunciation
        id = i.id
        list_audio.append(audio)
        list_word.append(word)
        list_image.append(image)
        list_pronunciation.append(pronunciation)
        list_id.append(id)
    return render_template("vegetablesAndFruits.html",
                            list_audio=list_audio,
                            list_word=list_word,
                            list_image=list_image,
                            list_pronunciation=list_pronunciation,
                            list_id=list_id,
                            user = user,
                           )

@app.route('/vegetablesAndFruitsDetail/<id>', methods = ["GET","POST"])
def vegetablesAndFruitsDetail(id):
    user = session.get('username')
    vegetables_fruits_id = Vegetablesfruits.objects.with_id(id)
   
    if request.method == "GET":
        return render_template("vegetablesAndFruitsDetail.html",
                                vegetables_fruits_id=vegetables_fruits_id,
                                user = user,
                               )
    else:
        if user is not None:
            wordReview = Reviews(
                image = vegetables_fruits_id.image,
                word = vegetables_fruits_id.word,
                pronunciation= vegetables_fruits_id.pronunciation,
                mean =vegetables_fruits_id.mean,
                audio_link = vegetables_fruits_id.audio_link,
                username = user
            )
            wordReview.save()        
            return redirect(url_for('vegetablesAndFruits'))  
        else:
            flash('You must login first !')
            return render_template("vegetablesAndFruitsDetail.html",
                                    vegetables_fruits_id=vegetables_fruits_id,
                                    user=user,
                                   ) 

@app.route('/animals')
def animals():
    user = session.get('username')
    list_audio = []
    list_word  = []
    list_image = []
    list_pronunciation = []
    list_id = []
     # get all document from dabase
    total_animals = Animals.objects()
    for i in total_animals:
        audio = i.audio_link
        word  = i.word
        image = i.image
        pronunciation = i.pronunciation
        id = i.id
        list_audio.append(audio)
        list_word.append(word)
        list_image.append(image)
        list_pronunciation.append(pronunciation)
        list_id.append(id)
    return render_template("animals.html",
                            list_audio=list_audio,
                            list_word=list_word,
                            list_image=list_image,
                            list_pronunciation=list_pronunciation,
                            list_id=list_id,
                            user=user,
                            )


@app.route('/animalDetail/<id>', methods = ["GET","POST"])
def animalDetail(id):
    user = session.get('username')
    animal_id = Animals.objects.with_id(id)
    
    if request.method == "GET":
        return render_template("animalDetail.html",
                                animal_id=animal_id,
                                user=user,
                                )
    else:
        if user is not None:
            wordReview = Reviews(
                image = animal_id.image,
                word = animal_id.word,
                pronunciation= animal_id.pronunciation,
                mean =animal_id.mean,
                audio_link = animal_id.audio_link,
                username = user
            )
            wordReview.save()        
            return redirect(url_for('animals'))
        else:
            flash('You must login first !')
            return render_template("animalDetail.html",
                                    animal_id=animal_id,
                                    user=user,
                                  ) 

if __name__ == '__main__':
    app.run(debug=True)