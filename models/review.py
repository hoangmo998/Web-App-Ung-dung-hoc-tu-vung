from mongoengine import Document,StringField 
class Reviews(Document):
    image = StringField()
    word = StringField()
    pronunciation = StringField()
    mean = StringField()
    audio_link = StringField()
    username = StringField()
