from mongoengine import Document,StringField 

class Actions(Document):
    image = StringField()
    word = StringField()
    pronunciation = StringField()
    mean = StringField()
    audio_link = StringField()
    example = StringField()