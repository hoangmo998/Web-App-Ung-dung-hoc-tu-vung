from flask import *
import bcrypt
from models.user import User
from models.vegetablesFruits import Vegetablesfruits
from models.animal import Animals
from models.action import Actions
from models.food import Food
from models.video import Video
from models.review import Reviews
from youtube_dl import YoutubeDL
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
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
    return render_template("navigation.html",
                            user=user,
                            numberOfWords=numberOfWords
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
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
    return render_template("learn.html",
                            user = user,
                            numberOfWords=numberOfWords
                           )

@app.route('/vegetablesAndFruits')
def vegetablesAndFruits():
    user = session.get('username')
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
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
                            numberOfWords=numberOfWords
                           )

@app.route('/vegetablesAndFruitsDetail/<id>', methods = ["GET","POST"])
def vegetablesAndFruitsDetail(id):
    user = session.get('username')
    vegetables_fruits_id = Vegetablesfruits.objects.with_id(id)
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
    if request.method == "GET":
        return render_template("vegetablesAndFruitsDetail.html",
                                vegetables_fruits_id=vegetables_fruits_id,
                                user = user,
                                numberOfWords=numberOfWords
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
                                    numberOfWords=numberOfWords
                                   ) 

@app.route('/animals')
def animals():
    user = session.get('username')
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
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
                            numberOfWords=numberOfWords
                            )


@app.route('/animalDetail/<id>', methods = ["GET","POST"])
def animalDetail(id):
    user = session.get('username')
    animal_id = Animals.objects.with_id(id)
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
    if request.method == "GET":
        return render_template("animalDetail.html",
                                animal_id=animal_id,
                                user=user,
                                numberOfWords=numberOfWords
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
                                    numberOfWords=numberOfWords
                                  ) 

@app.route('/food')
def food():
    user = session.get('username')
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
    list_audio = []
    list_word  = []
    list_image = []
    list_pronunciation = []
    list_id = []
     # get all document from dabase
    total_food = Food.objects()
    for i in total_food:
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
    return render_template("food.html",
                            list_audio=list_audio,
                            list_word=list_word,
                            list_image=list_image,
                            list_pronunciation=list_pronunciation,
                            list_id=list_id,
                            user=user,
                            numberOfWords=numberOfWords
                           )

@app.route('/foodDetail/<id>', methods = ["GET","POST"])
def foodDetail(id):
    user = session.get('username')
    food_id = Food.objects.with_id(id)
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
    if request.method == "GET":
        return render_template("foodDetail.html",
                                food_id=food_id,
                                user=user,
                                numberOfWords=numberOfWords
                                )
    else:
        if user is not None:
            wordReview = Reviews(
                image = food_id.image,
                word = food_id.word,
                pronunciation= food_id.pronunciation,
                mean =food_id.mean,
                audio_link = food_id.audio_link,
                username = user
            )
            wordReview.save()        
            return redirect(url_for('food'))
        else:
            flash('You must login first !')
            return render_template("foodDetail.html",
                                    food_id=food_id,
                                    user=user,
                                    numberOfWords=numberOfWords
                                ) 

@app.route('/actions')
def actions():
    user = session.get('username')
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
    list_audio = []
    list_word  = []
    list_image = []
    list_pronunciation = []
    list_id = []
     # get all document from dabase
    total_actions = Actions.objects()
    for i in total_actions:
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
    return render_template("actions.html",
                            list_audio=list_audio,
                            list_word=list_word,
                            list_image=list_image,
                            list_pronunciation=list_pronunciation,
                            list_id=list_id,
                            user=user,
                            numberOfWords=numberOfWords
                           )

@app.route('/actionsDetail/<id>', methods = ["GET","POST"])
def actionsDetail(id):
    user = session.get('username')
    actions_id = Actions.objects.with_id(id)
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
    if request.method == "GET":
        return render_template("actionsDetail.html",
                                actions_id=actions_id,
                                user=user,
                                numberOfWords=numberOfWords
                                )
    else:
        if user is not None:
            wordReview = Reviews(
                image = actions_id.image,
                word = actions_id.word,
                pronunciation= actions_id.pronunciation,
                mean =actions_id.mean,
                audio_link = actions_id.audio_link,
                username = user
            )
            wordReview.save()        
            return redirect(url_for('actions'))
        else:
            flash('You must login first !')
            return render_template("actionsDetail.html",
                                    actions_id=actions_id,
                                    user=user,
                                    numberOfWords=numberOfWords
                                 ) 

@app.route('/video')
def video():
    user = session.get('username')
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
   
    videos = Video.objects()
    return render_template("video.html",
                            videos = videos,
                            user = user,
                            numberOfWords=numberOfWords
                          )

@app.route('/detailVideo/<youtube_id>')
def detailVideo(youtube_id):
    user = session.get('username')
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
    return render_template("detailVideo.html",
                            youtube_id = youtube_id,
                            user = user,
                            numberOfWords=numberOfWords
                            )

@app.route('/review')
def review():
    user = session.get('username')
    allWordSave = Reviews.objects()
    numberOfWords = 0
    for i in allWordSave:
        if i.username == user:
            numberOfWords += 1
    return render_template("review.html",
                            user = user,
                            allWordSave = allWordSave,
                            numberOfWords=numberOfWords
                            )

@app.route('/deleteWord/<wordId>')
def deleteWord(wordId):
    word_delete_id = Reviews.objects.with_id(wordId)
    if word_delete_id is not None:
        word_delete_id.delete()
        return redirect(url_for('review'))
    else:
        return("Word not found")

@app.route('/admin', methods = ['GET','POST'])
def admin():
    user = session.get('username')
    if user is None:
        return redirect(url_for('login'))
    else:
        total_vegetablesAndFruits = Vegetablesfruits.objects()
        total_animals = Animals.objects()
        total_food = Food.objects()
        total_actions = Actions.objects()
        x = len(total_vegetablesAndFruits)
        y = len(total_animals)
        z = len(total_food)
        if request.method == 'GET':
            videos = Video.objects()
            return render_template("admin.html",
                                    total_vegetablesAndFruits = total_vegetablesAndFruits,
                                    total_animals = total_animals,
                                    total_food = total_food,
                                    total_actions = total_actions,
                                    x = x,
                                    y = y,
                                    z = z,
                                    videos = videos )
        elif request.method == 'POST':
            form = request.form
            link = form['link']

            ydl = YoutubeDL()

            data = ydl.extract_info(link, download=False)

            title = data['title']
            thumbnail = data['thumbnail']
            views = data['view_count']
            youtube_id = data['id']
            link = link
            video = Video( title = title,
                            thumbnail = thumbnail,
                            views = views,
                            youtube_id = youtube_id,
                            link = link,
                         )
            video.save()
            return redirect(url_for('admin'))

# delete word in adminWord
@app.route('/deleteVegetablesFruits/<id>')
def deleteVegetablesFruits(id):
    word_delete = Vegetablesfruits.objects.with_id(id)
    if word_delete is not None:
        word_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Word not found"

@app.route('/deleteAnimals/<id>')
def deleteAnimals(id):
    word_delete = Animals.objects.with_id(id)
    if word_delete is not None:
        word_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Word not found"

@app.route('/deleteFood/<id>')
def deleteFood(id):
    word_delete = Food.objects.with_id(id)
    if word_delete is not None:
        word_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Word not found"

@app.route('/deleteActions/<id>')
def deleteActions(id):
    word_delete = Actions.objects.with_id(id)
    if word_delete is not None:
        word_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Word not found"

@app.route('/deleteVideo/<id>')
def deleteVideo(id):
    video_id = Video.objects.with_id(id)
    if video_id is not None:
        video_id.delete()
        return redirect(url_for('admin'))
    else:
        return "video not found"

# Add word in adminWord
@app.route('/addWordVegetFruits', methods = ["GET","POST"])
def addWordVegetFruits():
    if request.method == "GET":
        return render_template("addWord.html")
    else:
        form = request.form
        add_word = Vegetablesfruits(
            image = form["image"],
            word = form["word"],
            pronunciation= form["pronunciation"],
            mean = form["mean"],
            audio_link = form["audio_link"],
        )
        add_word.save()
        return redirect(url_for('admin'))

@app.route('/addWordAnimals', methods = ["GET","POST"])
def addWordAnimals():
    if request.method == "GET":
        return render_template("addWord.html")
    else:
        form = request.form
        add_word = Animals(
            image = form["image"],
            word = form["word"],
            pronunciation= form["pronunciation"],
            mean = form["mean"],
            audio_link = form["audio_link"],
        )
        add_word.save()
        return redirect(url_for('admin'))

@app.route('/addWordFood', methods = ["GET","POST"])
def addWordFood():
    if request.method == "GET":
        return render_template("addWord.html")
    else:
        form = request.form
        add_word = Food(
            image = form["image"],
            word = form["word"],
            pronunciation= form["pronunciation"],
            mean = form["mean"],
            audio_link = form["audio_link"],
        )
        add_word.save()
        return redirect(url_for('admin'))

@app.route('/addWordActions', methods = ["GET","POST"])
def addWordActions():
    if request.method == "GET":
        return render_template("addWord.html")
    else:
        form = request.form
        add_word = Actions(
            image = form["image"],
            word = form["word"],
            pronunciation= form["pronunciation"],
            mean = form["mean"],
            audio_link = form["audio_link"],
        )
        add_word.save()
        return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)