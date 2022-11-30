#JSON (JavaScript Object Notation) is a lightweight data format for data exchange
#Compared to XML, JSON is much smaller, translating into faster data transfers, and better experiences
#below is converting from python to JSON
import json
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
#convert into JSON:
person_json = json.dumps(person)
#use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)
#the result is a JSON string:
print(person_json) 
print(person_json2) 
#creates new file which we can write in
with open('person.json', 'w') as file: 
    json.dump(person, file)

#decoding: converting from JSON to python
with open('person.json', 'r') as file:
    person = json.load(file) #loads is short for load string
print(person) #creates string


#working with a custom class Python to JSON
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#create user object
user = User('Ahmed', 24)

# function to translate class to dictionary to be converted to Json
def encode_user(o):
    if isinstance(o, User):
        return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

#dump as string
userJSON = json.dumps(user, default=encode_user) #calls the function
print(userJSON)


#another method
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

#dump as string
userJSON = json.dumps(user, cls=UserEncoder) #calls the class
print(userJSON)


#working with a custom class JSON to Python
#create a function that converts dict to User class
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(user.name)
