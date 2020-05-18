import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds263248.mlab.com:63248/vocabulary
host = "ds263248.mlab.com"
port = 63248
db_name = "vocabulary"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password,retryWrites= False)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())