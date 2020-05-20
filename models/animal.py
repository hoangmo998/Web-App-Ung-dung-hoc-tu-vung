from mongoengine import Document,StringField 
class Animals(Document):
    image = StringField()
    word = StringField()
    pronunciation = StringField()
    mean = StringField()
    audio_link = StringField()